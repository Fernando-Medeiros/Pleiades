<div align="center">
    <img align="center" src="https://img.shields.io/badge/Python-white?style=for-the-badge&logo=python&logoColor=yellow">
    <img align="center" src="https://img.shields.io/badge/Pygame-white?style=for-the-badge&logo=python&logoColor=orange">
</div>

<div align="center">
<h3>V.0.4</h3>
<img width=375 src="img/v.0.4.png">
</div>

<br>

# Pleiades Outpost

O posto avançado das Pleiades é um jogo do gênero **Tower Defense** no estilo espaço, cujo objetivo é **defender a base de naves inimigas** enquanto acumula pontos e se desenvolve.


> [Progresso do jogo ---> Tasks.md](tasks.md)

> [Imagens das versões](img/)

> [Ex. Imagem base do jogo](img/ex-base.png)


## Resumo
- [Pleiades Outpost](#pleiades-outpost)
  - [Resumo](#resumo)
  - [Requisitos](#requisitos)
  - [Ambiente](#ambiente)
  - [Iniciar o Jogo](#iniciar-o-jogo)
  - [Estrutura](#estrutura)
  - [Créditos](#créditos)


## Requisitos
- Git
- Python 3.10
- Pygame 2.1.2
- Virtualenv *ou semelhante*
- Um editor de códigos como VSCode, Sublime, Vim, Pycharm, etc...

> **Opicional**  -> blue 0.9.1  *Para formatar o codigo com flake8*

> **O .vscode** já possue configuração para auto formatação do flake8, portanto use o blue para complementar.

## Ambiente
Crie o ambiente virtual

```console
virtualenv .venv
```

Ative o ambiente 

```console
# Linux Bash
source .venv/bin/activate
# Windows Power Shell
./.venv/bin/activate.ps1
```

Instale as dependências

```console
pip install -r requirements.txt
```

## Iniciar o Jogo

```console
python main.py
```

## Estrutura

```console
.
├── docs
│   ├── img
│   │   ├── ex-base.png
│   │   ├── v.0.1.png
│   │   ├── v.0.2.png
│   │   ├── v.0.3_1.png
│   │   ├── v.0.3.png
│   │   └── v.0.4.png
│   ├── README.md
│   └── tasks.md
├── main.py
├── requirements.txt
├── src
│   ├── enemy
│   │   ├── entity.py
│   │   └── particles.py
│   ├── game.py
│   ├── layout
│   │   ├── hud.py
│   │   ├── menu.py
│   │   └── status.py
│   ├── player
│   │   ├── cannon.py
│   │   ├── entity.py
│   │   └── radius.py
│   └── stage
│       └── stages.py
└── static
    ├── image
    │   ├── credit.txt
    │   ├── nave1.png
    │   └── nave2.png
    └── soundtrack
        ├── credit.txt
        └── main.mp3

10 directories, 25 files
```

## Créditos

- [Soundtrack](/static/soundtrack/credit.txt)
- [Sprites](/static/image/credit.txt)