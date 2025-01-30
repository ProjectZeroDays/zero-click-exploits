import unittest
from unittest.mock import MagicMock
import tensorflow as tf
import numpy as np
from src.ai.ai_training import AITraining

class TestAITraining(unittest.TestCase):
    def setUp(self):
        self.model = MagicMock()
        self.data = np.random.rand(100, 10)
        self.labels = np.random.randint(2, size=100)
        self.ai_training = AITraining(self.model, self.data, self.labels)

    def test_train_model(self):
        self.ai_training.train_model(epochs=5, batch_size=16)
        self.model.fit.assert_called()

    def test_evaluate_model(self):
        self.model.predict.return_value = np.random.rand(20, 1)
        accuracy, precision, recall, f1 = self.ai_training.evaluate_model()
        self.assertIsInstance(accuracy, float)
        self.assertIsInstance(precision, float)
        self.assertIsInstance(recall, float)
        self.assertIsInstance(f1, float)

    def test_integrate_vLLM_models(self):
        self.ai_training.integrate_vLLM_models(['path/to/model1', 'path/to/model2'])
        self.assertEqual(len(self.ai_training.vllm_models), 2)

    def test_build_custom_dashboard(self):
        self.ai_training.vllm_models = [MagicMock(), MagicMock()]
        dashboard = self.ai_training.build_custom_dashboard()
        self.assertIn('vLLM_models', dashboard)
        self.assertIn('training_data', dashboard)
        self.assertIn('labels', dashboard)

if __name__ == '__main__':
    unittest.main()
