# 📡 ETL Radar AMMA — Retenção Preditiva com CRM Inteligente

Pipeline ETL com Python e Inteligência Artificial Generativa para transformar dados comportamentais em réguas de relacionamento e monitoramento de churn em tempo real.

---

## 💡 ETL com Inteligência de Negócios aplicada ao CX 

Este projeto apresenta uma forma moderna de aplicar o conceito de ETL (*Extract, Transform, Load*) no contexto de Customer Experience (CX) e Customer Relationship Management (CRM).

Em vez de trabalhar apenas com dados brutos de transações e acessos, o pipeline utiliza Inteligência Artificial Generativa para transformar o histórico de navegação e o tempo de ausência de clientes em um sistema preditivo de retenção, contendo diagnóstico de risco, definição estratégica de canal e mensagens altamente personalizadas de acolhimento. 

## A lógica principal é: 
    Dados de comportamento ➔ Enriquecimento com IA ➔ Réguas de relacionamento humanizadas


> 📌 **NOTA DE IMPLEMENTAÇÃO (VERSÃO ATUAL):**
> Para fins de demonstração, validação ágil de lógica e segurança de dados, esta versão do repositório executa o pipeline utilizando um **banco de dados interno simulado (Mocks)** com 15 perfis e matrizes de copywriting pré-definidas direto no código. 
> 
> A arquitetura do sistema foi modularizada para que a extração por arquivos `.csv` em lote e a geração de mensagens hiper-personalizadas via API de Inteligência Artificial (IA Generativa) funcionem como a próxima camada de atualização técnica, sem a necessidade de alterar a regra de negócio do Radar de Retenção aqui apresentada.


## 🎓 Novo Domínio: Retenção e Customer Success com ETL + IA 

O sistema foi desenhado para uma marca do ecossistema de bem-estar e skincare que recebe dados de engajamento e atividade dos clientes. Cada cliente possui informações cruciais como: 
* Nome completo
* E-mail e contato telefônico
* Tempo de ausência nas redes sociais (em dias)
* Último produto comprado
* Últimos produtos acessados no site
* Produto favorito (mais comprado)
* Último acesso ao site 
* Último produto salvo 
* Último produto abandonado (carrinho)


### O objetivo é rodar um pipeline ETL inteligente para:
* ✔️ Isolar automaticamente o primeiro nome para uma abordagem humanizada
* ✔️ Calcular o nível de risco de evasão (*churn*) baseado nos dias de ausência
* ✔️ Definir estrategicamente o canal de disparo ideal (E-mail ou WhatsApp)
* ✔️ Integrar com IA para gerar réguas de comunicação baseadas nos rituais de consumo de cada cliente
* ✔️ Alternar abordagens de forma dinâmica para evitar automações mecânicas
* ✔️ Salvar os relatórios e mensagens em formatos reutilizáveis para a equipe de CRM

---

## 🔄 Fluxo ETL

    📂 dados_ecommerce.csv
    Dados comportamentais dos clientes
             │
             ▼
    E — Extract
    Leitura e preparação dos dados com pandas
             │
             ▼
    T — Transform
    Análise preditiva e personalização de mensagens com IA
             │
             ▼
    L — Load
    Geração das planilhas e relatórios de CRM em Excel e JSON

## ⚙️ Detalhamento das Etapas
📩 E — Extract (Extração dos Dados)
A primeira etapa do ETL realiza a extração e leitura dos dados estruturados de comportamento e consumo dos clientes da base.

    Exemplo do formato de entrada:
    Plaintext
    Nome;Email;Contato;tempo_ausencia_redes_dias;ultimo_produto_comprado;ultimos_produtos_acessados;produto_mais_comprado
    Ana Silva;ana.silva@email.com;(11) 99999-1111;3;Sérum Vitamina C;Protetor Solar FPS 60;Sérum Vitamina C
    Carlos Souza;carlos@email.com;(41) 96666-4444;130;Creme Antissinais;Sérum Anti-Idade;Creme Antissinais

## Python
# Código conceitual de extração
import pandas as pd
    
    df_clientes = pd.read_csv("dados_ecommerce.csv", sep=";")
    
## 🧠 T — Transform (Transformação com IA)
A etapa de transformação é onde o ecossistema ganha inteligência e sensibilidade de escrita (UX Writing). O sistema avalia o histórico de cada cliente e simula o comportamento de um modelo de IA atuando como especialista em CRM e voz de marca.

    Python
    # Prompt conceitual enviado para a IA
    def generate_crm_ritual(row):
        prompt = f"""
        Você é um especialista em CRM e tom de voz acolhedor para marcas de autocuidado.
        Analise o comportamento do cliente e gere uma abordagem personalizada:
        
        Cliente: {row['Nome']}
        Tempo de ausência: {row['tempo_ausencia_redes_dias']} dias
        ...
        Retorne apenas um JSON válido com os campos: risco, tipo_disparo, mensagem.
        """
        return prompt
    
 - Exemplo de Saída da Inteligência (Alto Risco):

 - Risco: ALTO RISCO DE CHURN

 - Tipo de Disparo: WhatsApp (Exclusivo)

 - Mensagem: “Oi, Carlos. A vida corre lá fora, mas a pele se lembra do carinho que recebe. Sentimos falta de saber como você e o seu Creme Antissinais estão se adaptando. Quando sentir que é o momento de voltar a olhar para si com calma, preparamos um convite gentil no site. Use o código RITUALAMMA. Sem pressa. Com amor, AMMA.”

## 💾 L — Load (Carga dos Dados)
Depois que a inteligência de risco e as cópias personalizadas são consolidadas, o pipeline exporta os dados prontos para a equipe de Growth e Customer Experience agir, gerando planilhas estruturadas para ferramentas de disparo e arquivos JSON para automações de Webhooks.

    Python
    # Exportação do relatório final
    df_resultado = pd.DataFrame(dados_planilha)
    df_resultado.to_excel("resultado_radar_final.xlsx", index=False)
    
## 🚀 Próximos Passos & Evolução do Sistema (Roadmap)

O projeto foi arquitetado de forma modular para expandir a atual estrutura de testes para uma automação em larga escala através de duas frentes principais de integração e inteligência:

1. Integração Nativa com Ferramentas de CRM (Entrada e Saída): Substituição da base interna de testes por conexões automatizadas via API com plataformas de CRM (como HubSpot, Salesforce ou RD Station).

 • Na Extração: O pipeline passará a consumir diretamente em tempo real os dados de navegação, propriedades de contato e histórico de interações armazenados no CRM.

 • Na Carga: Em vez de apenas gerar planilhas, o sistema usará Webhooks e APIs para injetar os rituais e diagnósticos de risco direto na ficha do usuário dentro do CRM, ativando gatilhos automáticos de disparo omnicanal (E-mail, SMS ou WhatsApp).

2. Hiper-Personalização com Inteligência Artificial (IA): Integração via API com LLMs (como OpenAI ou Google Gemini) para substituir as matrizes dinâmicas por um motor generativo em tempo real. A IA interpretará o momento da jornada mapeado pelo CRM para redigir cópias exclusivas, poéticas e customizadas para cada régua de relacionamento de forma 100% humanizada.

## 🌟 Diferenciais de Negócio & Aplicação
Em vez de um relatório de CRM tradicional apenas com números frios, a equipe recebe um mapa de ação completo, compreensível e acionável sobre a situação de cada cliente. Esta solução foi desenhada para:
    
    - Marcas de E-commerce e D2C (Direct-to-Consumer)
    
    - Equipes de CRM, Marketing de Retenção e Customer Success (CS)
    
    - Programas e estratégias de combate à evasão de clientes (Anti-churn)

## 🛠️ Tecnologias Utilizadas
    - Python — Linguagem principal do projeto e controle do fluxo.
    
    - Pandas / Openpyxl — Leitura, manipulação, tratamento e exportação dos dados estruturados.
    
    - IA Generativa / UX Writing — Conceito de criação dinâmica de abordagens e escrita de conversação humanizada.
    
    - Git & GitHub — Controle de versão e documentação.

## 🎯 Contexto do Desafio
Este projeto foi desenvolvido como prática de aplicação de um fluxo de ETL inteligente voltado para Retenção de Clientes (Metodologia Radar). O foco principal é demonstrar como um fluxo clássico de dados pode ser adaptado para um domínio real, corporativo e útil: o Customer Experience. A solução mostra que ETL não precisa ser apenas extração, limpeza e armazenamento de dados frios. Com regras de negócio bem amarradas e sensibilidade de UX, o processo passa a gerar interpretação, diagnóstico e réguas de comunicação personalizadas.

> 📌 **NOTA DE IMPLEMENTAÇÃO & PORTFÓLIO:**
> Este repositório funciona como o portfólio estratégico da **Metodologia Radar**, demonstrando a arquitetura de dados e as entregas finais de CX. O script de automação em Python atua na camada de back-end (privado) para processar o pipeline ETL e gerar a inteligência. 
> 
> Para fins de demonstração pública, este espaço disponibiliza a massa de dados utilizada (`dados_ecommerce`), o relatório final gerado pelo sistema (`resultado_radar2_.xlsx`) e o detalhamento do tom de voz e regras de negócio aplicadas na régua de relacionamento.

    Desenvolvido com dedicação e Python por Isabelly Tertuliano.
