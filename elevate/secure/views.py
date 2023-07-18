from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import subprocess
import os


class SafetyCheckView(APIView):
    def post(self, request):
        requirements_content = request.data.get('requirements')
        if requirements_content:
            # Create a temporary requirements.txt file
            requirements_file_path = './requirements.txt'
            with open(requirements_file_path, 'w') as file:
                file.write(requirements_content)

            # Run safety check on the requirements.txt file
            cmd = ['safety', 'check', '-r', requirements_file_path]
            process = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            # Delete the temporary file
            os.remove(requirements_file_path)

            # Return the vulnerabilities as the API response
            vulnerabilities = stdout.decode('utf-8')
            return Response(vulnerabilities)
        else:
            return Response({'error': 'No requirements provided'}, status=400)
