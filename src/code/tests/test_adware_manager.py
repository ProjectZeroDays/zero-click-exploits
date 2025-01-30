import unittest
from unittest.mock import MagicMock
from src.dashboard.adware_dashboard.core.adware_manager import AdwareManager

class TestAdwareManager(unittest.TestCase):
    def setUp(self):
        self.logger = MagicMock()
        self.exploit_payloads = MagicMock()
        self.network_exploitation = MagicMock()
        self.adware_manager = AdwareManager(self.logger, self.exploit_payloads, self.network_exploitation)

    def test_create_adware(self):
        adware_config = self.adware_manager.create_adware("TestAdware", "TestPayload", "TestMethod")
        self.assertEqual(adware_config["name"], "TestAdware")
        self.assertEqual(adware_config["payload"], "TestPayload")
        self.assertEqual(adware_config["deployment_method"], "TestMethod")
        self.logger.info.assert_called_with(f"Adware created: {adware_config}")

    def test_deploy_adware(self):
        adware_config = {"name": "TestAdware", "payload": "TestPayload", "deployment_method": "TestMethod"}
        self.exploit_payloads.generate_payload.return_value = "GeneratedPayload"
        self.network_exploitation.deploy_payload.return_value = "DeploymentResult"
        deployment_result = self.adware_manager.deploy_adware(adware_config)
        self.assertEqual(deployment_result, "DeploymentResult")
        self.exploit_payloads.generate_payload.assert_called_with("TestPayload")
        self.network_exploitation.deploy_payload.assert_called_with("GeneratedPayload", "TestMethod")
        self.logger.info.assert_called_with(f"Adware deployment result: DeploymentResult")

    def test_add_device_control_panel(self):
        control_panel = self.adware_manager.add_device_control_panel("TestDevice", {"feature1": "value1"})
        self.assertEqual(control_panel["device_name"], "TestDevice")
        self.assertEqual(control_panel["control_features"], {"feature1": "value1"})
        self.logger.info.assert_called_with(f"Device control panel added: {control_panel}")

    def test_manage_device_control_panels(self):
        self.adware_manager.device_control_panels = [
            {"device_name": "Device1", "control_features": {"feature1": "value1"}},
            {"device_name": "Device2", "control_features": {"feature2": "value2"}}
        ]
        self.adware_manager.manage_device_control_panels()
        self.logger.info.assert_any_call("Managing device control panels")
        self.logger.info.assert_any_call("Device control panel: {'device_name': 'Device1', 'control_features': {'feature1': 'value1'}}")
        self.logger.info.assert_any_call("Device control panel: {'device_name': 'Device2', 'control_features': {'feature2': 'value2'}}")

if __name__ == "__main__":
    unittest.main()
