
# Instruções para Configuração do Projeto

Este guia fornece as etapas para configurar um ambiente virtual, instalar as dependências e rodar o projeto Python com Django e pyserial.

## 1. Criar um Ambiente Virtual

Antes de instalar as bibliotecas necessárias, crie um ambiente virtual. Isso isola as dependências do projeto das outras instalações Python no sistema.

### Passos:

1. No terminal, navegue até o diretório do projeto:

   ```bash
   cd /caminho/do/seu/projeto
   ```

2. Crie o ambiente virtual usando `venv`:

   ```bash
   python -m venv env
   ```

   Isso criará uma pasta chamada `env` contendo o Python e as bibliotecas específicas do projeto.

3. Ative o ambiente virtual:

   - **No Windows**:

     ```bash
     env\Scripts\activate
     ```

   - **No macOS/Linux**:

     ```bash
     source env/bin/activate
     ```

   Após a ativação, o nome do ambiente virtual (`env`) aparecerá no início do prompt do terminal.

## 2. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Este comando instalará as bibliotecas listadas, como o Django e o pyserial.

## 3. Rodar o Projeto

Após configurar o ambiente, você pode rodar o servidor Django:

```bash
python manage.py runserver
```

Acesse o projeto no navegador em `http://127.0.0.1:8000/`.

## 4. Desativar o Ambiente Virtual

Para desativar o ambiente virtual quando terminar, use o comando:

```bash
deactivate
```

Isso encerrará a sessão do ambiente virtual.
