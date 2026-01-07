#método para adicionar tarefa
    def adicionar_tarefa(self, tarefa):
        se não tarefa ou tarefa.strip() == "":
            retornar Falso

        auto . tarefas_registradas . anexar ({
            "nome" : tarefa . strip (),
            "status" : "pendente"
        })
        retornar Verdadeiro

    #método para remover a tarefa
    def removedor_tarefa(self, índice):
        if 0 <= índice < len(self.tarefas_registradas):
            self.tarefas_registradas.pop(índice)
            retornar Verdadeiro
        retornar Falso