TF_BIN := terraform
PLAN_FILE := plan.tfplan

init-plan: init plan

init:
	@$(TF_BIN) init

plan:
	@$(TF_BIN) plan -out=$(PLAN_FILE)

apply:
	@$(TF_BIN) apply $(PLAN_FILE)

deploy: init plan apply

destroy:
	@$(TF_BIN) destroy

run-api:
	@echo "Running API"
	@python main.py
