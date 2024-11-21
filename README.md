# 🚀 **AP3-Unifametro-Project** 🚀

Bem-vindo ao repositório do **Projeto de Inovação Tecnológica** da disciplina de **Projeto de Inovação Tecnológica** da **Unifametro**! Este projeto apresenta uma solução inovadora que visa automatizar o controle de ar condicionado com base na detecção de pessoas em tempo real, aplicando a metodologia **PMBOK** para garantir excelência no planejamento, gestão e entrega do projeto.

### 🎯 **Objetivo do Projeto**

O principal objetivo deste projeto é desenvolver uma aplicação inteligente que utiliza a tecnologia de **detecção de pessoas** para ativar e desativar o ar condicionado de forma automática, proporcionando conforto e eficiência energética em ambientes corporativos ou salas de aula.

### 🛠️ **Tecnologias Utilizadas**

- **YOLOv8**: Utilizado para detecção em tempo real de pessoas no vídeo capturado pela câmera.
- **OpenCV**: Para manipulação de imagens e vídeos, exibindo informações sobre a detecção de pessoas e status do ar condicionado.
- **Python 3.x**: A linguagem principal do projeto, devido à sua simplicidade e poderosas bibliotecas para visão computacional.
- **PMBOK**: Metodologia de gerenciamento de projetos para garantir que a execução seja eficaz e a entrega atenda aos requisitos.

### 📈 **Funcionalidades Principais**

- **Detecção de Pessoas em Tempo Real**: Utiliza o modelo YOLOv8 para identificar e contar o número de pessoas presentes no ambiente.
- **Controle Automático do Ar Condicionado**: O ar condicionado é ativado automaticamente quando o número de pessoas atinge um limite específico e desativado após um tempo configurável de inatividade.
- **Exibição Dinâmica de Dados**: O número de pessoas e o status do ar condicionado são exibidos diretamente no vídeo em tempo real.
- **Interface Interativa**: Ao visualizar o vídeo, o usuário pode facilmente entender a operação do sistema através das informações visuais exibidas na tela.

### 🚀 **Metodologia PMBOK**

Este projeto foi desenvolvido com base na metodologia **PMBOK**, garantindo que as fases de planejamento, execução e controle fossem bem definidas. As etapas do projeto seguiram os seguintes pilares:

- **Gerenciamento de Tempo**: Planejamento eficiente das etapas do desenvolvimento.
- **Gerenciamento de Custos**: Controle rigoroso do orçamento do projeto.
- **Gerenciamento de Riscos**: Identificação e mitigação dos riscos potenciais durante o ciclo de vida do projeto.

### 🧰 **Requisitos**

Para rodar o projeto localmente, você vai precisar dos seguintes requisitos:

- Python 3.x
- OpenCV
- YOLOv8 (modelo de detecção de objetos)
- Outros pacotes e dependências podem ser encontrados no arquivo `requirements.txt`.

### 📝 **Como Rodar**

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/davifdev085/AP3-Unifametro-Project
    ```

2. **Instale as dependências**:

    Navegue até o diretório do projeto e instale as bibliotecas necessárias:

    ```bash
    pip install -r requirements.txt
    ```

3. **Baixe o modelo YOLOv8**:

    Baixe o arquivo do modelo **YOLOv8** (por exemplo, `yolov8n.pt`) e coloque-o no diretório `model/`.

4. **Execute o programa**:

    Para rodar o sistema de controle de ar condicionado com detecção de pessoas:

    ```bash
    python main.py
    ```

5. **Saia do programa**:

    Durante a execução, se desejar parar o sistema, basta pressionar `Q` para sair.

### 🔧 **Configurações Personalizáveis**

- **Tempo para desligar o ar condicionado**: O tempo que o ar condicionado permanece ligado após a detecção de pessoas pode ser configurado no código.
- **Número mínimo de pessoas para ativação**: O limite de pessoas para acionar o ar condicionado também é configurável.

### 📊 **Gerenciamento de Riscos e Entregas**

A aplicação do **PMBOK** proporcionou um planejamento robusto e uma visão clara dos riscos. Os seguintes aspectos foram considerados durante o desenvolvimento:

- **Riscos Técnicos**: Garantir que a detecção de pessoas funcione corretamente em diferentes condições de luz e ângulos de câmera.
- **Riscos de Implementação**: Garantir que o controle do ar condicionado seja preciso e com baixo tempo de latência.
- **Gerenciamento de Cronograma e Custos**: Controle rigoroso das atividades e prazos, com entregas em etapas.

### 🎨 **Exemplo de Imagem**

em breve

*Exemplo de como a contagem de pessoas e o status do ar condicionado são exibidos no vídeo.*

### 🚧 **Contribuições**

Este projeto foi desenvolvido para fins acadêmicos. No entanto, contribuições são sempre bem-vindas! Se você quiser melhorar ou sugerir novas funcionalidades, fique à vontade para abrir uma **issue** ou enviar um **pull request**.

### 📜 **Licença**

Em Breve

---

🔗 **Link para o repositório:** [GitHub - AP3-Unifametro-Project](<https://github.com/davifdev085/AP3-Unifametro-Project>)

---

**Este projeto reflete um exemplo prático e eficaz de como a tecnologia pode ser aplicada para resolver problemas do cotidiano com eficiência e inovação.**
