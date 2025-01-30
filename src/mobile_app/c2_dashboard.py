import React, { useState, useEffect } from 'react';
import { View, Text, Button, StyleSheet, FlatList, TextInput, Alert } from 'react-native';
import axios from 'axios';
import io from 'socket.io-client';
import * as Notifications from 'expo-notifications';
import * as Permissions from 'expo-permissions';

const C2Dashboard = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [authToken, setAuthToken] = useState('');
  const [command, setCommand] = useState('');
  const [deviceId, setDeviceId] = useState('');
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    authenticateUser();
    initializeWebSocket();
    registerForPushNotifications();
  }, []);

  const authenticateUser = async () => {
    try {
      const response = await axios.post('https://your-api-endpoint.com/auth', {
        username: 'your-username',
        password: 'your-password',
      });
      setAuthToken(response.data.token);
      fetchData(response.data.token);
    } catch (error) {
      console.error('Error during authentication:', error);
      setLoading(false);
    }
  };

  const fetchData = async (token) => {
    try {
      const response = await axios.get('https://your-api-endpoint.com/data', {
        headers: { Authorization: `Bearer ${token}` },
      });
      setData(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching data:', error);
      setLoading(false);
    }
  };

  const initializeWebSocket = () => {
    const socketInstance = io('https://your-api-endpoint.com');
    socketInstance.on('connect', () => {
      console.log('WebSocket connected');
    });
    socketInstance.on('notification', (notification) => {
      Alert.alert('Notification', notification.message);
    });
    setSocket(socketInstance);
  };

  const registerForPushNotifications = async () => {
    const { status } = await Permissions.askAsync(Permissions.NOTIFICATIONS);
    if (status !== 'granted') {
      Alert.alert('Permission not granted', 'You need to grant notification permissions to receive alerts.');
      return;
    }
    const token = (await Notifications.getExpoPushTokenAsync()).data;
    console.log('Push notification token:', token);
    // Send the token to your backend server for registration
  };

  const sendCommand = async () => {
    try {
      const response = await axios.post(
        'https://your-api-endpoint.com/command',
        { deviceId, command },
        { headers: { Authorization: `Bearer ${authToken}` } }
      );
      Alert.alert('Command sent', response.data.message);
    } catch (error) {
      console.error('Error sending command:', error);
      Alert.alert('Error', 'Failed to send command');
    }
  };

  const renderItem = ({ item }) => (
    <View style={styles.item}>
      <Text style={styles.title}>{item.title}</Text>
      <Text>{item.description}</Text>
    </View>
  );

  return (
    <View style={styles.container}>
      {loading ? (
        <Text>Loading...</Text>
      ) : (
        <>
          <FlatList
            data={data}
            renderItem={renderItem}
            keyExtractor={(item) => item.id.toString()}
          />
          <TextInput
            style={styles.input}
            placeholder="Device ID"
            value={deviceId}
            onChangeText={setDeviceId}
          />
          <TextInput
            style={styles.input}
            placeholder="Command"
            value={command}
            onChangeText={setCommand}
          />
          <Button title="Send Command" onPress={sendCommand} />
        </>
      )}
      <Button title="Refresh" onPress={() => fetchData(authToken)} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  item: {
    backgroundColor: '#f9c2ff',
    padding: 20,
    marginVertical: 8,
    marginHorizontal: 16,
  },
  title: {
    fontSize: 32,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
    width: '80%',
  },
});

export default C2Dashboard;
