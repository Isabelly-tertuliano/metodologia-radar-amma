## 📡 ETL Radar AMMA — Retenção Preditiva com CRM Inteligente ##
Pipeline ETL com Python e Engenharia de Recursos para transformar dados comportamentais de e-commerce em réguas de relacionamento poéticas e monitoramento de churn em tempo real.

💡 ETL com Inteligência de Negócios aplicada ao CX
Este projeto apresenta uma forma moderna de aplicar o conceito de ETL — Extract, Transform, Load no contexto de Customer Experience (CX) e Customer Relationship Management (CRM).

Em vez de trabalhar apenas com dados frios de transações e acessos, o pipeline utiliza regras de negócio automatizadas e escrita de conversação (UX Writing) para transformar o histórico de navegação e o tempo de ausência de clientes em um sistema preditivo de retenção. O foco é gerar rituais de acolhimento personalizados, identificando riscos de evasão e definindo o canal ideal de disparo para cada perfil.

## A lógica principal é:
    dados de comportamento → inteligência de risco com CRM → réguas de relacionamento humanizadas

##🎓 Domínio: Retenção e Customer Success com ETL
O sistema atua simulando o ecossistema de uma marca de skincare (AMMA), que monitora a atividade e o engajamento de sua base de clientes.

##Cada perfil possui informações como:
Nome completo do cliente
E-mail e contato telefônico
Tempo de ausência nas redes (em dias)
Último produto comprado
Últimos produtos acessados/namorados no site
Produto favorito (mais comprado)

## O objetivo é rodar um pipeline ETL inteligente e transmutável para: 
✔️ Isolar automaticamente o primeiro nome para uma abordagem humanizada
✔️ Calcular o nível de risco de evasão (churn) baseado nos dias de ausência
✔️ Definir estrategicamente o canal de disparo ideal (E-mail ou WhatsApp)
✔️ Tecer réguas de comunicação poéticas e personalizadas com os produtos do histórico do cliente
✔️ Alternar abordagens de forma randômica para evitar automações mecânicas
✔️ Salvar os relatórios prontos em arquivos reutilizáveis e dinâmicos de Excel (.xlsx)

##🔄 Fluxo ETL:
    
    📂 dados_ecommerce.csv (ou Estrutura de Dados Nativa)
    Dados comportamentais e rituais de consumo dos clientes
    │
    ▼
    E — Extract
    Leitura, normalização e preparação dos dados direto na memória do Python
    │
    ▼
    T — Transform
    Análise preditiva de risco (Radar), segmentação de canais e geração de cópias personalizadas
    │
    ▼
    L — Load
    # Geração dos relatórios consolidados em planilhas Excel estruturadas por carimbo de tempo # 

[1_projeto_RADAR.py](https://github.com/user-attachments/files/28330952/1_projeto_RADAR.py)
# metodologia-radar-ammaimport time
    import random
    import pandas as pd 
    print("=== ETAPA 1: EXTRAÇÃO (Carregando Dados) ===")
    
    # ==========================================
    # 0. CONTEXTO DE BRANDING DA MARCA (AMMA)
    # ==========================================
    BRIEFING = """Estratégia de CRM: Régua de Retenção Preventiva (Radar de Evasão)
    Objetivo: Agir de forma preventiva na retenção da base, 
    utilizando a classificação do Radar de Evasão (desenvolvido em Python) para reengajar o cliente de maneira sutil, 
    personalizada e alinhada ao tom de voz acolhedor da AMMA.
    
    A régua funciona de forma modular e omnichannel, 
    ativando o canal mais adequado (E-mail ou WhatsApp) conforme o nível de necessidade e o score de risco do cliente:
    
    Risco Baixo: Foco em E-mail Marketing, 
    trazendo conteúdos ricos sobre rituais e autocuidado para manter a marca presente na rotina de forma leve.
    
    Risco Médio: Abordagem de escuta e suporte, 
    utilizando E-mail ou WhatsApp para entender o momento de uso do produto e oferecer auxílio na jornada de cuidados.
    
    Risco Alto: Ação direta de resgate via WhatsApp, 
    focada em acolhimento e na oferta de um benefício exclusivo para facilitar o retorno do cliente à marca.
    
    Abaixo, estão mapeados os templates e mensagens de disparo para cada cenário. 
    """
    print(BRIEFING) 
    print("-"*50)
    
    dados_clientes = [
        {
            "Nome": "Ana Silva",
            "Email": "ana.silva@email.com",
            "Contato": "(11) 99999-1111",
            "tempo_ausencia_redes_dias": 3,
            "ultimo_produto_comprado": "Sérum Vitamina C",
            "ultimos_produtos_acessados": "Protetor Solar FPS 60",
            "produto_mais_comprado": "Sérum Vitamina C"
        },
        {
            "Nome": "Beatriz Lima",
            "Email": "beatriz.lima@email.com",
            "Contato": "(21) 98888-2222",
            "tempo_ausencia_redes_dias": 22,
            "ultimo_produto_comprado": "Gel de Limpeza Facial",
            "ultimos_produtos_acessados": "Tônico Renovador",
            "produto_mais_comprado": "Gel de Limpeza Facial"
        },
        {
            "Nome": "Carlos Souza",
            "Email": "carlos.souza@email.com",
            "Contato": "(41) 96666-4444",
            "tempo_ausencia_redes_dias": 130,
            "ultimo_produto_comprado": "Creme Antissinais Firmador",
            "ultimos_produtos_acessados": "Sérum Anti-Idade",
            "produto_mais_comprado": "Creme Antissinais Firmador"
        },
        {
            "Nome": "Mariana Costa",
            "Email": "mariana.costa@email.com",
            "Contato": "(31) 97777-3333",
            "tempo_ausencia_redes_dias": 2,
            "ultimo_produto_comprado": "Protetor Solar FPS 60",
            "ultimos_produtos_acessados": "Sérum Ácido Salicílico",
            "produto_mais_comprado": "Protetor Solar FPS 60"
        },
        {
            "Nome": "Juliana Reis",
            "Email": "juliana.reis@email.com",
            "Contato": "(51) 95555-5555",
            "tempo_ausencia_redes_dias": 15,
            "ultimo_produto_comprado": "Bálsamo Labial Hidratante",
            "ultimos_produtos_acessados": "Óleo Facial Noturno",
            "produto_mais_comprado": "Bálsamo Labial Hidratante"
        },
        {
            "Nome": "Fernanda Dias",
            "Email": "fernanda.dias@email.com",
            "Contato": "(11) 94444-6666",
            "tempo_ausencia_redes_dias": 4,
            "ultimo_produto_comprado": "Espuma de Limpeza Suave",
            "ultimos_produtos_acessados": "Água Micelar Calmante",
            "produto_mais_comprado": "Espuma de Limpeza Suave"
        },
        {
            "Nome": "Ricardo Alves",
            "Email": "ricardo.alves@email.com",
            "Contato": "(11) 93333-7777",
            "tempo_ausencia_redes_dias": 45,
            "ultimo_produto_comprado": "Sérum Ácido Hialurônico",
            "ultimos_produtos_acessados": "Creme Área dos Olhos",
            "produto_mais_comprado": "Sérum Ácido Hialurônico"
        },
        {
            "Nome": "Camila Rocha",
            "Email": "camila.rocha@email.com",
            "Contato": "(19) 92222-8888",
            "tempo_ausencia_redes_dias": 1,
            "ultimo_produto_comprado": "Máscara de Argila Rosa",
            "ultimos_produtos_acessados": "Esfoliante Facial Enzimático",
            "produto_mais_comprado": "Máscara de Argila Rosa"
        },
        {
            "Nome": "Lucas Martins",
            "Email": "lucas.martins@email.com",
            "Contato": "(21) 91111-9999",
            "tempo_ausencia_redes_dias": 60,
            "ultimo_produto_comprado": "Hidratante Nutritivo",
            "ultimos_produtos_acessados": "Óleo de Limpeza (Cleansing Oil)",
            "produto_mais_comprado": "Hidratante Nutritivo"
        },
        {
            "Nome": "Gabriela Meireles",
            "Email": "gabi.meireles@email.com",
            "Contato": "(31) 90000-0000",
            "tempo_ausencia_redes_dias": 12,
            "ultimo_produto_comprado": "Tônico Renovador",
            "ultimos_produtos_acessados": "Sérum Vitamina C",
            "produto_mais_comprado": "Tônico Renovador"
        },
        {
            "Nome": "Patricia Antunes",
            "Email": "paty.antunes@email.com",
            "Contato": "(47) 98989-1234",
            "tempo_ausencia_redes_dias": 35,
            "ultimo_produto_comprado": "Protetor Solar FPS 60",
            "ultimos_produtos_acessados": "Bálsamo Labial Hidratante",
            "produto_mais_comprado": "Protetor Solar FPS 60"
        },
        {
            "Nome": "Bruno Fonseca",
            "Email": "bruno.fonseca@email.com",
            "Contato": "(11) 97878-5678",
            "tempo_ausencia_redes_dias": 180,
            "ultimo_produto_comprado": "Gel de Limpeza Facial",
            "ultimos_produtos_acessados": "Sérum Ácido Salicílico",
            "produto_mais_comprado": "Gel de Limpeza Facial"
        },
        {
            "Nome": "Amanda Vieira",
            "Email": "amanda.v@email.com",
            "Contato": "(21) 96767-9012",
            "tempo_ausencia_redes_dias": 5,
            "ultimo_produto_comprado": "Sérum Niacinamide 10%",
            "ultimos_produtos_acessados": "Protetor Solar FPS 60",
            "produto_mais_comprado": "Sérum Niacinamide 10%"
        },
        {
            "Nome": "Rodrigo Melo",
            "Email": "rodrigo.melo@email.com",
            "Contato": "(81) 95656-3456",
            "tempo_ausencia_redes_dias": 8,
            "ultimo_produto_comprado": "Creme Antissinais Firmador",
            "ultimos_produtos_acessados": "Sérum Ácido Hialurônico",
            "produto_mais_comprado": "Creme Antissinais Firmador"
        },
        {
            "Nome": "Larissa Cavalcanti",
            "Email": "lari.c@email.com",
            "Contato": "(85) 94545-7890",
            "tempo_ausencia_redes_dias": 29,
            "ultimo_produto_comprado": "Bruma Hidratante Conforto",
            "ultimos_produtos_acessados": "Máscara de Argila Rosa",
            "produto_mais_comprado": "Bruma Hidratante Conforto"
        }
    ]
    
    print(f"✅ {len(dados_clientes)} perfis de pele carregados direto do código.\n")
    
    
    # ==========================================
    # ETAPA 2: TRANSFORMAÇÃO (Processamento)
    # ==========================================
    print("=== ETAPA 2: TRANSFORMAÇÃO (Mensagens Poéticas e Canais) ===")
    
    dados_planilha = []
    
    # O loop agora percorre a lista de dados internos com segurança total
    for cliente in dados_clientes:
    
    nome_completo = cliente['Nome']
    email_cliente = cliente['Email']      
    contato_cliente = cliente['Contato']  
    ausencia = int(cliente['tempo_ausencia_redes_dias'])
    ultimo_produto = cliente['ultimo_produto_comprado']
    ultimo_acesso = cliente['ultimos_produtos_acessados']
    produto_favorito = cliente['produto_mais_comprado']
    
    # Classificação de Risco e Canal de Disparo
    if ausencia <= 5:
        risco_calculado = "BAIXO RISCO DE CHURN"
        tipo_disparo = "E-mail"
    elif 6 <= ausencia <= 40:
        risco_calculado = "MEDIO RISCO DE CHURN"
        tipo_disparo = "WhatsApp"
    else:
        risco_calculado = "ALTO RISCO DE CHURN"
        tipo_disparo = "WhatsApp (Exclusivo)"
        
    primeiro_nome = nome_completo.split()[0]
    
    # Mensagens mockadas simplificadas para o teste rodar 100% sem erros de digitação
    mensagem_escolhida = f"Oi, {primeiro_nome}. Notamos que faz {ausencia} dias que não nos visitamos. Sentimos falta do seu momento AMMA com o seu {produto_favorito}."

    # BANCO DE MOCK INSPIRADO NO MANIFESTO DA AMMA
    if risco_calculado == "BAIXO RISCO DE CHURN":
        opcoes = [
            f"Oi, {primeiro_nome}. Que o seu {ultimo_produto} seja um momento de pausa hoje. Notamos que você olhou o {ultimo_acesso} no site... Se quiser conversar sobre como ele se adapta ao seu ritual atual, estamos aqui. Sem pressa. Com afeto, AMMA.",
            f"Oi, {primeiro_nome}. A pele sente o ritmo dos nossos dias. Que tal estender o cuidado do seu {ultimo_produto} experimentando a textura fluida do {ultimo_acesso}? Um passo de cada vez no seu pacto de gentileza com o espelho. AMMA.",
            f"Oi, {primeiro_nome}. Validamos a sua jornada e o tempo que você dedica a si mesma. Seu {ultimo_produto} ganhou um espaço na sua rotina, e deixamos o {ultimo_acesso} guardado como uma sugestão suave para o seu próximo amanhecer. AMMA."
        ]
    elif risco_calculado == "MEDIO RISCO DE CHURN":
        opcoes = [
            f"Oi, {primeiro_nome}. Como está a sua pele nesta estação? Sentimos que o ciclo do seu querido {produto_favorito} pode estar pedindo uma renovação. Lembre-se de olhar para o espelho com calma e notar o que o seu corpo pede hoje. AMMA.",
            f"Oi, {primeiro_nome}. O autocuidado é um pacto diário que não tem pressa. Passando para acompanhar de perto como a sua pele tem respondido ao {produto_favorito}. Se for a hora de reabastecer esse momento sensorial, nosso espaço te espera com calma. AMMA.",
            f"Oi, {primeiro_nome}. Nossos rituais nos devolvem a presença no mundo. Se o seu {produto_favorito} estiver chegando ao fim, encare a reposição como mais um gesto de carinho e respeito pelo seu próprio tempo. Estamos aqui para te acompanhar. AMMA."
        ]
    else: # Alto risco
        opcoes = [
            f"Oi, {primeiro_nome}. A vida corre lá fora, mas a pele se lembra do carinho que recebe. Sentimos falta de saber como você e o seu {produto_favorito} estão se adaptando. Quando sentir que é o momento de voltar a esse abraço em forma de rotina, use o código RITUALAMMA. Sem pressa. AMMA.",
            f"Oi, {primeiro_nome}. Entendemos que a pele reage às estações e às emoções da sua jornada. Faz tempo que não nos visitamos, mas o seu afeto pelo {produto_favorito} ficou guardado em nossa memória. Preparamos um mimo suave para quando você decidir pausar e voltar ao espelho. AMMA.",
            f"Oi, {primeiro_nome}. Desejamos presença para o seu dia hoje. Sentimos falta do seu momento AMMA. Se o seu coração pedir um reencontro com o aroma e a eficácia com propósito do seu {produto_favorito}, preparamos um convite gentil em nosso site. Com amor, AMMA."
        ]
    
    mensagem_escolhida = random.choice(opcoes)
    # INDENTAÇÃO CORRETA: Guarda as informações de CADA um na lista enquanto roda o loop
    dados_planilha.append({
        "primeiro_nome": primeiro_nome,
        "email": email_cliente,
        "contato": contato_cliente,
        "risco": risco_calculado,
        "tipo_disparo": tipo_disparo,
        "mensagem": mensagem_escolhida
    })
    
    print(f" Processando disparo ESTILO AMMA para: {nome_completo} -> mensagem Adicionada com sucesso.")

    print(f"\n✅ Todos os {len(dados_planilha)} perfis foram processados com sucesso!")
    
    
    # ==========================================
    # ETAPA 3: CARGA (Salvando no Excel com Nome Único)
    # ==========================================
    print("\n=== ETAPA 3: CARGA (Gerando o Planilha) ===")
    
    # Converte toda a lista acumulada para um DataFrame
    df_resultado = pd.DataFrame(dados_planilha)
    
    # Carimbo de hora para evitar travar no cache antigo do Excel
    nome_saida_excel = f"resultado_radar1_.xlsx"
    
    # Gravação definitiva do arquivo
    df_resultado.to_excel(nome_saida_excel, index=False)
    
    print(f"📊 Planilha '{nome_saida_excel}' gerada!")
    print(f"📁 Total de linhas gravadas na planilha: {len(df_resultado)}")
    print("🚀 PIPELINE COMPLETADO A 100%!")

## 🌟 Por que esse domínio é poderoso? ##
Com um único pipeline ETL, uma marca pode transformar dados simples de navegação em informação estratégica de retenção e relacionamento de alto valor.

## Este projeto permite: ##
✔️ Acompanhar o engajamento dos clientes de forma mais inteligente e preditiva
✔️ Identificar riscos de evasão (churn) com bastante antecedência
✔️ Apoiar equipes de CRM e Customer Success na tomada de decisão rápida
✔️ Gerar réguas de relacionamento muito mais humanas, poéticas e personalizadas
✔️ Orientar as abordagens comerciais com recomendações práticas de produtos
✔️ Entregar relatórios claros e prontos para a execução das equipes de disparo
Em vez de um relatório de CRM tradicional apenas com números frios, a equipe recebe uma análise completa, compreensível e acionável sobre a situação de cada cliente.

## 👥 Este tipo de solução pode ser usado por ##
Marcas de E-commerce e D2C (Direct-to-Consumer)
Equipes de CRM e Marketing de Retenção
Gestores de Customer Success (CS) e Customer Experience (CX)
Plataformas de Automação de Marketing
Projetos de Growth Hacking
Programas e estratégias de combate à evasão de clientes

## 🚀 Possibilidades de Expansão ##

    O projeto foi desenhado de forma transmutável e pode evoluir para soluções ainda mais complexas, como:
    ✔️ Integração direta com APIs de IA Generativa (OpenAI, Gemini) para criar mensagens dinâmicas em tempo real
    ✔️ Conexão direta com Bancos de Dados (PostgreSQL, MySQL) ou leitura automatizada de arquivos em nuvem
    ✔️ Envio automático dos rituais integrando com APIs de mensageria (HubSpot, WhatsApp, Outlook, N8N)
    ✔️ Dashboard em Power BI com taxas de risco por segmento e histórico de retenção
    ✔️ Criação de um banco de dados histórico para acompanhar a evolução do cliente ao longo do ano
    ✔️ Classificação automática de risco acadêmico/comercial refinada por inteligência preditiva
    ✔️ Recomendações específicas baseadas em inteligência de recomendação de produtos

## 🛠️ Tecnologias utilizadas##
    
    | Tecnologia | Função |
    | :--- | :--- |
    | **Python** | Linguagem principal do projeto e controle do fluxo |
    | **pandas** | Leitura, manipulação e tratamento dos dados estruturados |
    | **random & datetime** | Geração dinâmica de abordagens e carimbo de tempo para relatórios únicos |
    | **Excel (.xlsx)** | Armazenamento estruturado e saída tabular pronta para uso das equipes |
    | **VS Code** | Ambiente de desenvolvimento e execução do pipeline |

## 🎯 Contexto do Desafio ##
    Este projeto foi desenvolvido como prática de aplicação de um fluxo de ETL inteligente voltado para Retenção de Clientes (Metodologia Radar).
    O foco principal é demonstrar como um fluxo clássico de dados pode ser adaptado para um domínio real, corporativo e útil: o Customer Experience.
    A solução mostra que ETL não precisa ser apenas extração, limpeza e armazenamento de dados frios. Com regras de negócio bem amarradas e sensibilidade de UX, o processo passa a gerar interpretação, diagnóstico e réguas de comunicação personalizadas.

Em resumo:
## O projeto transforma dados comportamentais simples em planilhas de relacionamento inteligentes, ajudando marcas a tomarem decisões melhores e a reconectarem clientes aos seus rituais de cuidado de forma humana. ##
