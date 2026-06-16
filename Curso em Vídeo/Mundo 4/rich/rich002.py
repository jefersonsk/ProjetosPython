from rich import print
from rich.panel import Panel

caixa = Panel("[white]Esse é um painel de exemplo![/]:+1:", title="Mensagem", style="red", width=35)

print(caixa)