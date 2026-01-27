# REMOVER ARTE GERADA — instruções seguras (PowerShell)

Observação importante:

- Eu não consigo remover arquivos binários existentes no workspace por limitação do ambiente aqui.
- Você pode executar estes comandos localmente no seu repositório para remover todos os arquivos gerados por mim, revisar e commitar.

1. Entre no root do seu repositório (onde está o .git):

```powershell
Set-Location 'C:\projects\spreadsheet_improvements'
```

1. Lista de arquivos gerados (confirme antes de apagar):

```powershell
Get-Content assets\store_listing\TO_DELETE_BY_REQUEST.txt
```

1. Apague e faça commit (PowerShell):

```powershell
# Remove arquivos listados
Get-Content assets\store_listing\TO_DELETE_BY_REQUEST.txt | ForEach-Object { Remove-Item -Force $_ }

# Remova também do Git e commite
git rm -r --cached -f assets/store_listing
git add -A
git commit -m "chore(store): remove generated store assets per request"
git push origin HEAD
```

1. (Opcional) Se quiser, recrie uma pasta limpa para novos rascunhos:

```powershell
New-Item -ItemType Directory -Path assets\store_listing\final -Force
```

Se preferir, posso gerar um script .ps1 pronto para executar — diga e eu o crio aqui para você baixar.



Se concordar, prossigo agora e gerarei novas propostas de alta qualidade numa pasta separada (assets/store_listing/final/) sem tocar nos arquivos existentes até você executar a remoção ou pedir que eu o faça quando o repo estiver sob controle Git no ambiente. Se quiser que eu gere o script .ps1, diga "gerar script".
