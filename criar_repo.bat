@echo off

setlocal

:: Defina suas informações de usuário do Git
set GIT_USER=micaelcosmo
set GIT_EMAIL=micael.trabalho@hotmail.com

:: Defina o nome do seu novo repositório
set REPO_NAME=raindrop-python

:: Inicialize o Git dentro da nova pasta
git init

:: Adicione um novo arquivo README.md
echo # %REPO_NAME% > README.md

:: Adicione um novo repositório remoto no GitHub
git remote add origin https://github.com/micaelcosmo/%REPO_NAME%.git

:: Faça o commit do arquivo README.md
git add .
git commit -m "Adicionado arquivo README.md"

:: Faça o push do commit para o GitHub
git push -u origin master

pause
