/* eslint-disable react-native/no-inline-styles */
import React from 'react';
import {Button, StyleSheet, Text, TextInput, View} from 'react-native';
import {createStackNavigator, createAppContainer} from 'react-navigation';

class LoginPage extends React.Component {
  render() {
    return (
      <View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
        <Text style={styles.defaultStyle}>Dr. Paw's Vet App</Text>
        <View>
          <Text>Username</Text>
          <TextInput placeholder="Username" />
        </View>
        <View>
          <Text>Password</Text>
          <TextInput placeholder="Password" />
        </View>
        <View>
          <Button
            title="Login"
            onPress={() => this.props.navigation.navigate('Home')}
          />
          <Button
            title="Create an account"
            onPress={() => this.props.navigation.navigate('Signup')}
          />
        </View>
      </View>
    );
  }
}

class SignUpPage extends React.Component {
  render() {
    return (
      <View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
        <Text>Create your account(Fields with a * are required)</Text>
        <View>
          <Text>First Name*</Text>
          <TextInput placeholder="First Name" />
        </View>
        <View>
          <Text>Last Name*</Text>
          <TextInput placeholder="Last Name" />
        </View>
        <View>
          <Text>Phone Number</Text>
          <TextInput placeholder="(XXX)-XXX-XXXX" />
        </View>
        <View>
          <Text>Email*</Text>
          <TextInput placeholder="Your email" />
        </View>
        <View>
          <Text>Username*</Text>
          <TextInput placeholder="Your desired username" />
        </View>
        <View>
          <Text>Password*</Text>
          <TextInput placeholder="Your password" />
        </View>
        <Text>
          Passwords must be 8-12 characters long and contain a mix of capital
          and lowercase letters, numbers, and symbols. They must not contain
          your username or any personal information.
        </Text>
        <View>
          <Button
            title="Create Account"
            onPress={() => {
              this.props.navigation.navigate('Login');
              this.alert('Account created. Please login.');
            }}
          />
          <Button
            title="Back to Login"
            onPress={() => this.props.navigation.navigate('Login')}
          />
        </View>
      </View>
    );
  }
}

class HomePage extends React.Component {
  render() {
    return (
      <View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
        <Text>Home Page</Text>
        <View>
          <Button
            title="Account Settings"
            onPress={() => {
              this.props.navigation.navigate('AccountInfo');
            }}
          />
          <Button
            title="Pet Profiles"
            onPress={() => {
              this.props.navigation.navigate('Pet Profiles');
            }}
          />
          <Button
            title="Appointments"
            onPress={() => {
              this.props.navigation.navigate('Appointments');
            }}
          />
          <Button
            title="Messages"
            onPress={() => {
              this.props.navigation.navigate('Messages');
            }}
          />
          <Button
            title="Reminders"
            onPress={() => {
              this.props.navigation.navigate('Reminders');
            }}
          />
        </View>
      </View>
    );
  }
}

class AccountInfoPage extends React.Component {}

class PetProfileList extends React.Component {}

class AppointmentList extends React.Component {}

class MessageList extends React.Component {}

class ReminderList extends React.Component {}

const styles = StyleSheet.create({
  defaultStyle: {
    color: 'black',
    fontSize: 24,
  },
});

const MainNavigator = createStackNavigator({
  Login: {screen: LoginPage},
  Signup: {screen: SignUpPage},
  Home: {screen: HomePage},
  AccountInfo: {screen: AccountInfoPage},
  PetProfiles: {screen: PetProfileList},
  Appointments: {screen: AppointmentList},
  Messages: {screen: MessageList},
  Reminders: {screen: ReminderList},
  initialRouteName: 'Login',
});

const AppContainer = createAppContainer(MainNavigator);
export default class App extends React.Component {
  render() {
    return <AppContainer />;
  }
}
