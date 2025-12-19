from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['features_para_quem'] = [
            'Sentem que o relacionamento esfriou ou se tornou distante',
            'Vivem conflitos recorrentes, má comunicação ou silêncios dolorosos',
            'Estão cansadas de carregar tudo sozinhas',
            'Desejam restaurar a relação sem se anular',
            'Querem amadurecer emocionalmente, com mais clareza e segurança',
            'Amam, mas não sabem mais como se conectar',
        ]
        
        context['sobre_texto'] = """
        Terapeuta especializado em relacionamentos, com formação em Ciência da Família pela CIM. 
        Atuo no cuidado emocional de indivíduos e casais, com foco em relacionamentos, maturidade emocional e responsabilidade afetiva.
        
        Meu trabalho é voltado para ajudar mulheres e casais a compreenderem seus padrões emocionais, 
        reorganizarem a comunicação e criarem relações mais conscientes, respeitosas e possíveis.
        
        Acredito que relacionamentos podem ser restaurados quando existe espaço para escuta, clareza emocional 
        e compromisso com o amadurecimento — individual e relacional. Minha postura clínica é acolhedora, 
        ética e direta, oferecendo segurança emocional para que mudanças reais aconteçam.
        """

        context['beneficios'] = [
            'Mais clareza emocional',
            'Comunicação mais madura',
            'Redução da ansiedade e da sobrecarga emocional',
            'Relações mais equilibradas e conscientes',
            'Segurança para se posicionar sem culpa',
            'Autonomia emocional dentro do relacionamento',
        ]
        
        # Adicione outras listas de features conforme necessário
        return context
