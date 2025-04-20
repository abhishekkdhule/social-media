

import os
from rest_framework import serializers
from cryptography.fernet import Fernet
import firebase_admin
from firebase_admin import credentials, firestore, auth

cred = credentials.Certificate("firebaseConfig.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

class UserSignupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=6, max_length=128)
    confirm_password = serializers.CharField(write_only=True, max_length=128)

    def is_valid(self, *, raise_exception=True):
        super().is_valid(raise_exception=raise_exception)
        if self.initial_data['password'] != self.initial_data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return True
    
    def save(self, **kwargs):
        # key = os.environ.get('fernet_key')
        # cipher_suite = Fernet(key)
        # encrypted_password = cipher_suite.encrypt(self.validated_data['password'].encode())
        userCreds = auth.create_user(
            email=self.validated_data['email'],
            password=self.validated_data['password'],
            display_name=self.validated_data['name']
        )
        db.collection('users').document(self.validated_data['email']).set({
                    'name': self.validated_data['name'],
                    'email': self.validated_data['email'],
                    # 'password': encrypted_password.decode() 
                })   
        
        return
    

class UserSigninSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, max_length=128)

    def is_valid(self, *, raise_exception=True):
        super().is_valid(raise_exception=raise_exception)
        auth.sign_in_with_email_and_password(self.validated_data['email'], self.validated_data['password'])
        # user_doc = db.collection('users').document(self.validated_data['email']).get()
        # if not user_doc.exists:
        #     raise serializers.ValidationError({"email": "User does not exist."})
        # key = os.environ.get('fernet_key')
        # cipher_suite = Fernet(key)
        # decrypted_password = cipher_suite.decrypt(user_doc.to_dict()['password'].encode()).decode()
        # if decrypted_password != self.validated_data['password']:
        #     raise serializers.ValidationError({"password": "Incorrect password."})
        # return True
    
    