import random

# Base de conhecimento: 50 pares (pergunta -> resposta)
faq = {
    "o que é doação de sangue?": "É o ato voluntário de ceder uma pequena quantidade de sangue para ajudar pacientes que necessitam de transfusão.",
    "quem pode doar sangue?": "Pessoas entre 16 e 69 anos, com peso acima de 50 kg e boas condições de saúde.",
    "menores de idade podem doar sangue?": "Sim, entre 16 e 17 anos, desde que tenham autorização formal dos responsáveis.",
    "qual é a idade mínima para doar sangue?": "A idade mínima é de 16 anos, com consentimento do responsável.",
    "qual é a idade máxima para doar sangue?": "69 anos, sendo que a primeira doação deve ter sido feita até os 60.",
    "qual o peso mínimo para doar sangue?": "É necessário ter pelo menos 50 kg.",
    "quantas vezes por ano posso doar sangue?": "Homens podem doar até 4 vezes por ano e mulheres até 3 vezes.",
    "qual o intervalo entre doações de sangue?": "Homens precisam esperar 60 dias e mulheres 90 dias entre as doações.",
    "quanto sangue é coletado em uma doação?": "São coletados cerca de 450 ml de sangue.",
    "doar sangue dói?": "Não, apenas um pequeno desconforto na hora da picada da agulha.",
    "quem não pode doar sangue?": "Pessoas com doenças transmissíveis pelo sangue, grávidas, lactantes ou com problemas de saúde temporários.",
    "grávidas podem doar sangue?": "Não, mulheres grávidas não podem doar sangue.",
    "quem teve covid pode doar sangue?": "Sim, desde que tenha se recuperado e esteja sem sintomas há pelo menos 10 dias.",
    "quem tomou vacina da covid pode doar sangue?": "Sim, mas precisa respeitar um intervalo de 2 a 7 dias dependendo da vacina.",
    "pode doar sangue gripado?": "Não, é preciso estar totalmente recuperado.",
    "quem fez tatuagem pode doar sangue?": "Sim, mas deve aguardar 12 meses após a tatuagem.",
    "quem usa piercing pode doar sangue?": "Sim, desde que o piercing tenha sido colocado há mais de 12 meses.",
    "quem usa medicamento pode doar sangue?": "Depende do medicamento, alguns impedem temporariamente a doação.",
    "quanto tempo leva a doação de sangue?": "O processo completo leva em torno de 40 minutos.",
    "quantos minutos dura a coleta de sangue?": "A coleta em si dura cerca de 10 a 15 minutos.",
    "precisa estar em jejum para doar sangue?": "Não, deve-se estar alimentado e evitar comidas gordurosas antes da doação.",
    "precisa apresentar documento para doar sangue?": "Sim, é necessário documento oficial com foto.",
    "pode beber álcool antes de doar sangue?": "Não, é necessário estar sem consumir álcool nas últimas 12 horas.",
    "pode fumar antes de doar sangue?": "Sim, mas é recomendado não fumar 2 horas antes da doação.",
    "doar sangue faz mal?": "Não, o organismo repõe rapidamente o sangue retirado.",
    "quanto tempo o corpo leva para repor o sangue?": "O plasma é reposto em até 24 horas e os glóbulos vermelhos em algumas semanas.",
    "quem tem pressão alta pode doar sangue?": "Sim, se estiver controlada e com acompanhamento médico.",
    "quem tem diabetes pode doar sangue?": "Se controlada e sem complicações, é permitido doar sangue.",
    "quem tem anemia pode doar sangue?":"Não, é necessário estar com níveis adequados de hemoglobina.",
    "quem fez cirurgia pode doar sangue?": "Depende do tipo de cirurgia, o intervalo varia de 3 a 12 meses.",
    "doar sangue emagrece?": "Não, doar sangue não faz emagrecer.",
    "doar sangue engorda?": "Não, doar sangue não faz engordar.",
    "quanto tempo depois de doar posso praticar exercícios?": "É recomendado aguardar pelo menos 12 horas antes de atividades físicas intensas.",
    "doar sangue transmite doenças": "Não, os materiais usados são descartáveis e esterilizados.",
    "qual é o tipo de sangue mais raro": "O AB negativo.",
    "qual é o tipo de sangue mais comum": "O O positivo.",
    "qual tipo de sangue doa para todos": "O O negativo é considerado doador universal.",
    "qual tipo de sangue recebe de todos": "O AB positivo é considerado receptor universal.",
    "qual a diferença entre sangue total e hemocomponentes": "O sangue pode ser usado inteiro ou separado em hemocomponentes (plasma, plaquetas, hemácias).",
    "quem recebe sangue": "Pacientes em cirurgias, acidentes, anemias graves, câncer, entre outros.",
    "posso doar sangue se estiver menstruada": "Sim, não há problema em doar sangue durante a menstruação.",
    "posso doar sangue se estiver tomando anticoncepcional": "Sim, o uso de anticoncepcionais não impede a doação.",
    "posso doar sangue amamentando": "Não, mulheres que estão amamentando não podem doar sangue.",
    "quem tem hepatite pode doar sangue": "Quem teve hepatite após os 11 anos não pode doar sangue.",
    "qual é a frequência de doação de plaquetas": "Pode ser feita a cada 15 dias, até 24 vezes por ano.",
    "quem doa sangue ganha atestado": "Sim, a lei garante dispensa de um dia de trabalho no caso da doação.",
    "quem doa sangue recebe dinheiro": "Não, a doação é um ato voluntário e altruísta.",
    "qual o principal benefício de doar sangue": "Salvar vidas de pessoas que necessitam de transfusão.",
    "por que é importante doar sangue": "Porque o sangue não pode ser fabricado artificialmente e muitas pessoas dependem da doação.",
    "onde posso doar sangue": "Em hemocentros e hospitais credenciados em sua cidade."
}

# Função para responder
def responder(pergunta):
    pergunta = pergunta.lower().strip()
    if pergunta in faq:
        return faq[pergunta]
    else:
        return "Desculpe, não entendi sua pergunta. Pode reformular?"

# Loop de interação
print("🤖 Chatbot FAQ sobre Doação de Sangue")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")
    if pergunta.lower() == "sair":
        print("Chatbot: Obrigado por conversar! Até logo.")
        break
    resposta = responder(pergunta)
    print("Chatbot:", resposta)
