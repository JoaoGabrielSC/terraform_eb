# Setup project
- Clone the repository
- Create the virtual environment
```bash	
python3.11 -m venv venv
```
- Activate the virtual environment on Windows or Linux with pyenv
```bash
.\venv\Scripts\activate
pyenv activate venv
```
- Install the requirements
```bash
pip install -r requirements.txt
```
- Run the project
```bash
python main.py
```
- Go to the browser and type the following URL
```bash
http://localhost:3000/docs
```
- You will see the Swagger UI, where you can test the API

# Terraform Makefile and API Deployment

This Makefile helps automate Terraform operations such as initialization, planning, applying changes, and optionally destroying infrastructure. It also includes a command to run a Python API (`main.py`).

## Variables:
- **TF_BIN**: Defines the Terraform binary command, defaulting to `terraform`.
- **PLAN_FILE**: Specifies the output plan file name for Terraform (`plan.tfplan`).

## Makefile Targets:
1. **`init-plan`**: 
    Apply changes based on the saved plan (`plan.tfplan`).
   - Default target to initialize Terraform and generate a plan.
   - Depends on the `init` and `plan` targets.

2. **`init`**: 
   - Initializes the Terraform working directory (fetches modules, providers, etc.).
   - Command: `terraform init`

3. **`plan`**: 
   - Generates a Terraform execution plan and saves it to a file (`plan.tfplan`).
   - Command: `terraform plan -out=plan.tfplan`

4. **`apply`**: 
    Full deployment (initialize, plan, apply)
   - Applies the Terraform changes based on the generated plan (`plan.tfplan`).
   - Command: `terraform apply plan.tfplan`

5. **`deploy`**: 
   - Combines the `init`, `plan`, and `apply` steps in one target, allowing a full deployment with a single command.
   - Command: `make deploy`

6. **`destroy`**: 
   - Optionally destroys the Terraform-managed infrastructure. Use this with caution as it will remove all resources.
   - Command: `terraform destroy`

7. **`run-api`**: 
   - Runs the Python API (`main.py`).
   - Command: `python main.py`

## Usage:

### Initialize and plan infrastructure:
```bash
    make init-plan
    make apply
    make deploy
    make run-api
```
