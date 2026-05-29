import time
import random
import pandas as pd 

PROJETO = """
======================================================================
  METODOLOGIA RADAR DE RETENÇÃO — PIPELINE DE AUTOMAÇÃO MULTICANAL
======================================================================
OBJETIVO DO RADAR:
Identificar proativamente os riscos de evasão (churn) de clientes da 
AMMA Skincare através do tempo de ausência. O sistema segmenta a base 
em réguas de saúde (Baixo, Médio e Alto Risco) e estrutura rituais 
estratégicos dinâmicos de copywriting (E-mail e WhatsApp) focados 
em conversão, experiência do usuário (UX Writing) e resgate de marca.

COMO ACONTECE (PIPELINE ETL):
1. EXTRAÇÃO: O script lê os dados brutos e histórico de compras da base.
2. TRANSFORMAÇÃO: Avalia o risco, define o canal ideal e sorteia layouts 
   completos (Assunto, Preview, Título e CTAs específicos).
3. CARGA: Exibe os rituais processados e gera um relatório consolidado 
   em Excel para munir o time de Marketing.
======================================================================
Iniciando processamento dos perfis e briefing da marca...
"""
print(PROJETO) 
# ==========================================
# 0. CONTEXTO DE BRANDING DA MARCA (AMMA)
# ==========================================
BRIEFING = """ 
Estratégia de CRM: Régua de Retenção Preventiva (Radar de Evasão)
Objetivo: Agir de forma preventiva na retenção da base, 
utilizando a classificação do Radar de Evasão (desenvolvido em Python) 
para reengajar o cliente de maneira sutil, 
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

print("\n=== ETAPA 1: EXTRAÇÃO (Carregando Dados) ===")
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
print("\n=== ETAPA 2: TRANSFORMAÇÃO (Mensagens Poéticas e Canais) ===")

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
    
# 🧠 BANCO DE MOCK INSPIRADO NO MANIFESTO DA AMMA
    if risco_calculado == "BAIXO RISCO DE CHURN":
        opcoes = [
            {
                "assunto": f"Uma pausa para a sua pele, {primeiro_nome}? 🌿",
                "preview": f"Notamos que você olhou o {ultimo_acesso} no site...",
                "mensagem": f"Oi, {primeiro_nome}. Que o seu {ultimo_produto} seja um momento de pausa hoje. Notamos que você olhou o {ultimo_acesso} no site... Se quiser conversar sobre como ele se adapta ao seu ritual atual, estamos aqui. Sem pressa. Com afeto, AMMA.",
                "cta": "Ir para o site"
            },
            {
                "assunto": f"O ritmo dos dias e o seu momento AMMA 🌸",
                "preview": "Um passo de cada vez no seu pacto de gentileza.",
                "mensagem": f"Oi, {primeiro_nome}. A pele sente o ritmo dos nossos dias. Que tal estender o cuidado do seu {ultimo_produto} experimentando a textura fluida do {ultimo_acesso}? Um passo de cada vez no seu pacto de gentileza com o espelho. AMMA.",
                "cta": "Ir para o site"
            },
            {
                "assunto": f"Validamos a sua jornada com afeto ✨",
                "preview": f"O seu {ultimo_produto} tem um convite para hoje.",
                "mensagem": f"Oi, {primeiro_nome}. Validamos a sua jornada e o tempo que você dedica a si mesma. Seu {ultimo_produto} ganha um novo significado quando combinado com o carinho que sua pele pede agora. AMMA.",
                "cta": "Ir para o site"
            }
        ]
        escolha = random.choice(opcoes)
        assunto_final = escolha["assunto"]
        preview_final = escolha["preview"]
        mensagem_final = escolha["mensagem"]
        cta_final = escolha["cta"]
        titulo_final = "Não se aplica"

    elif risco_calculado == "MEDIO RISCO DE CHURN":
        opcoes = [
            {
                "titulo": "⚠️ ALERTA DE RENOVAÇÃO DO SEU RITUAL",
                "mensagem": f"Oi, {primeiro_nome}. Como está a sua pele nesta estação? Sentimos que o ciclo do seu querido {produto_favorito} pode estar pedindo uma renovação. Lembre-se de olhar para o espelho com calma e notar o que o seu corpo pede hoje. AMMA.",
                "cta": "Conversar com vendedor"
            },
            {
                "titulo": "🌸 UM GENTIL LEMBRETE DE AUTOCUIDADO",
                "mensagem": f"Oi, {primeiro_nome}. O autocuidado é um pacto diário que não tem pressa. Passando para acompanhar de perto como a sua pele tem respondido ao {produto_favorito}. Se precisar de ajuda para ajustar a rotina, estamos online. AMMA.",
                "cta": "Conversar com vendedor"
            },
            {
                "titulo": "✨ PRESENÇA E CONEXÃO NO SEU DIA",
                "mensagem": f"Oi, {primeiro_nome}. Nossos rituais nos devolvem a presença no mundo. Se o seu {produto_favorito} estiver chegando ao fim, não quebre esse ciclo de carinho. Vamos renovar juntas? AMMA.",
                "cta": "Ir para o site"
            }
        ]
        escolha = random.choice(opcoes)
        titulo_final = escolha["titulo"]
        mensagem_final = escolha["mensagem"]
        cta_final = escolha["cta"]
        assunto_final = "Não se aplica"
        preview_final = "Não se aplica"

    else: # Alto risco
        opcoes = [

            {
                "titulo": "🚨 SENTIMOS SUA FALTA POR AQUI...",
                "mensagem": f"Oi, {primeiro_nome}. A vida corre lá fora, mas a pele se lembra do carinho que recebe. Sentimos falta de saber como você e o seu {produto_favorito} estão se adaptando. Quando sentir que é o momento de voltar, use o código RITUALAMMA. Sem pressa. AMMA.",
                "cta": "Conversar com vendedor"
            },
            {
                "titulo": "🌿 RECONECTANDO SEU MOMENTO AMMA",
                "mensagem": f"Oi, {primeiro_nome}. Entendemos que a pele reage às estações e às emoções da sua jornada. Faz tempo que não nos vemos, e adoraríamos entender o momento atual da sua pele para te indicar o melhor caminho. AMMA.",
                "cta": "Conversar com vendedor"
            },
            {
                "titulo": "🤍 UM CONVITE REPLETO DE AFETO",
                "mensagem": f"Oi, {primeiro_nome}. Desejamos presença para o seu dia hoje. Sentimos falta do seu momento AMMA. Se o seu coração pedir um reencontro com o aroma do seu {produto_favorito}, preparamos um convite gentil e exclusivo para você. Com amor, AMMA.",
                "cta": "Ir para o site"
            }
      
        ]
        escolha = random.choice(opcoes)
        titulo_final = escolha["titulo"]
        mensagem_final = escolha["mensagem"]
        cta_final = escolha["cta"]
        assunto_final = "Não se aplica"
        preview_final = "Não se aplica"

    print(f"Processando disparo ESTILO AMMA para: {nome_completo} -> Mensagem Adicionada com sucesso.")

    dados_planilha.append(
         {
         "primeiro_nome": primeiro_nome,
         "email": email_cliente,
         "contato": contato_cliente,
         "risco": risco_calculado,
         "tipo_disparo": tipo_disparo,
         "assunto": assunto_final,
         "preview": preview_final,
         "titulo_whatsapp": titulo_final,
         "mensagem": mensagem_final,
         "cta": cta_final
        }
    )
    print("\n" + "="*60)
    print(f"👤 CLIENTE PROCESSADO: {primeiro_nome} | Canal: {tipo_disparo}")
    print(f"🚨 STATUS NO RADAR: {risco_calculado}")
    print("="*60)
    
    if tipo_disparo == "E-mail":
        print(f"📬 ASSUNTO: {assunto_final}")
        print(f"👀 PREVIEW: {preview_final}")
        print(f"📝 CORPO DO E-MAIL:\n{mensagem_final}")
        print(f"⚡ [BOTÃO CTA]: {cta_final}")
    else:
        print(f"💬 TÍTULO WHATSAPP: {titulo_final}")
        print(f"📝 MENSAGEM DO CHAT:\n{mensagem_final}")
        print(f"🔗 [AÇÃO DO CLIENTE]: {cta_final}")
        
    print("="*60 + "\n")

# 📥 LOGO ABAIXO, TOTALMENTE ENCOSTADO NA MARGEM ESQUERDA (FORA DO LOOP):
print(f"\n✅ Todos os {len(dados_planilha)} perfis foram processados com sucesso!")

# 📥 SÓ A ETAPA 3 (SALVAR O EXCEL) FICA ENCOSTADA NA ESQUERDA, FORA DO LOOP:
print("\n=== ETAPA 3: CARGA ===")

# Cria o DataFrame com todos os dados acumulados
df_resultado = pd.DataFrame(dados_planilha)

# Define o nome do arquivo final como texto (com aspas)
nome_saida_excel = "resultado_radar3_.xlsx"

# Salva o arquivo Excel de verdade
df_resultado.to_excel(nome_saida_excel, index=False)

print(f"📊 Planilha '{nome_saida_excel}' gerada!")
print(f"📁 Total de linhas gravadas na planilha: {len(df_resultado)}")
print("🚀 PIPELINE COMPLETADO A 100%!")
