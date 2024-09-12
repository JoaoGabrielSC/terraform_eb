# Variável
TF_BIN := terraform
PLAN_FILE := plan.tfplan

# Alvo padrão
init-plan: init plan

# Inicializar Terraform
init:
	@$(TF_BIN) init

# Mostrar o plano do Terraform e salvar em um arquivo
plan:
	@$(TF_BIN) plan -out=$(PLAN_FILE)

# Aplicar as mudanças do Terraform usando o arquivo de plano salvo
apply:
	@$(TF_BIN) apply $(PLAN_FILE)

# Faz tudo de uma vez
deploy: init plan apply

# Limpar o estado do Terraform (opcional, use com cautela)
destroy:
	@$(TF_BIN) destroy


# api run main.py
run-api:
	@echo "Running API"
	@python main.py
