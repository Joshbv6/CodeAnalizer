@echo off

cd ./Docker

docker build -t codeanalizer_image .

docker-compose -p codeanalizer_project up -d

powershell -command "& {Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('App has been installed succesfully!')}"

start http://localhost:8000


