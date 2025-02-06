import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class DataVisualization:
    def __init__(self):
        sns.set(style="whitegrid")

    def plot_device_information(self, device_data):
        df = pd.DataFrame(device_data)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="device_type", y="count", data=df)
        plt.title("Device Information")
        plt.xlabel("Device Type")
        plt.ylabel("Count")
        plt.show()

    def plot_network_traffic(self, traffic_data):
        df = pd.DataFrame(traffic_data)
        plt.figure(figsize=(10, 6))
        sns.lineplot(x="timestamp", y="traffic", hue="protocol", data=df)
        plt.title("Network Traffic")
        plt.xlabel("Timestamp")
        plt.ylabel("Traffic")
        plt.show()

    def plot_system_logs(self, log_data):
        df = pd.DataFrame(log_data)
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
        plt.title("System Logs Correlation")
        plt.show()

    def plot_threat_detection(self, threat_data):
        df = pd.DataFrame(threat_data)
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x="timestamp", y="severity", hue="threat_type", data=df)
        plt.title("Threat Detection")
        plt.xlabel("Timestamp")
        plt.ylabel("Severity")
        plt.show()

    def plot_defcon_level(self, defcon_data):
        df = pd.DataFrame(defcon_data)
        plt.figure(figsize=(10, 6))
        sns.lineplot(x="timestamp", y="defcon_level", data=df)
        plt.title("Defcon Level Status")
        plt.xlabel("Timestamp")
        plt.ylabel("Defcon Level")
        plt.show()
