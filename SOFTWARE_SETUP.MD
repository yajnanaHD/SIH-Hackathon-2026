# SIH-Hackathon-2026 — Environment Setup Guide

This guide gets the Software (perception) track running on a fresh Windows machine. Follow it top to bottom — skipping steps is how you end up debugging the same issues we already fought through.

## Prerequisites

- Python 3.11 or 3.12 recommended (avoid brand-new releases like 3.14 — some ML libraries lag behind on compatibility)
- Git installed
- VS Code (or your editor of choice)

## 1. Clone the repo

```powershell
git clone <repo-url>
cd SIH-Hackathon-2026
```

## 2. Allow PowerShell to run local scripts (one-time, per machine)

Windows blocks `.ps1` scripts by default. Run this once in PowerShell:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Type `Y` when prompted. This only affects your user account and is a standard, safe setting for development machines.

## 3. Set up `.gitignore` (first person to set up the repo only)

Before creating your venv, make sure it never gets committed to Git — it's machine-specific and can be gigabytes in size. Create a `.gitignore` file in the repo root containing at least:
```
venv/
__pycache__/
*.pyc
*.pt
```
(The `*.pt` line ignores downloaded model weight files too — those should be re-downloaded per machine, not committed, unless the team decides otherwise for a specific final model.)

If you're joining a repo where this already exists, skip this step.

## 4. Create a virtual environment

Do this inside the `SOFTWARE` folder (or repo root — match wherever `main.py` lives):

```powershell
python -m venv venv
```

## 5. Activate it

```powershell
.\venv\Scripts\Activate.ps1
```

You'll know it worked when your prompt shows `(venv)` at the start. **You must do this every time you open a new terminal** — it doesn't stay active permanently.

## 6. Install dependencies

**If `requirements.txt` already exists in the repo** (someone on the team already generated it), just run:
```powershell
pip install -r requirements.txt
```
and skip to step 7.

**If this is the first setup and `requirements.txt` doesn't exist yet**, install packages manually:
```powershell
pip install ultralytics opencv-python
```
(Add other packages here as the project grows — e.g. `mavsdk` once the flight-control integration starts.)

Then generate the requirements file for everyone else:
```powershell
pip freeze > requirements.txt
```
Commit this file to the repo. It's just a text list of package names + versions (~40 lines is normal — installing `ultralytics` pulls in PyTorch, OpenCV, and all of *their* dependencies too). Nothing sensitive in it — safe to commit.

**Whenever you install a new package later**, re-run `pip freeze > requirements.txt` and commit the updated file, so the team stays in sync.

## 7. Verify the install

```powershell
yolo checks
```

This should print your Python version, PyTorch version, and CUDA availability (CUDA `False` is fine on non-GPU laptops — inference will just run on CPU). If this command fails, see Troubleshooting below.

## 8. Run a sanity check

```powershell
yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
```

This downloads a small pretrained model and runs detection on a sample image. If it completes and saves an output image with boxes drawn, your environment is fully working.

---

## Troubleshooting

**`yolo` command not recognized**
Your terminal isn't seeing the `yolo.exe` script. Make sure your venv is activated (`(venv)` should be visible in the prompt). If it's still not found outside a venv, the Scripts folder for your Python install isn't in PATH — ask in the team chat rather than fighting it alone, it's usually a 2-minute fix once someone looks at it.

**`ModuleNotFoundError: No module named 'ultralytics'`**
This almost always means `pip install` and the `python`/`yolo` command are pointing to *different* Python installations on your machine (common if you have more than one Python version installed, e.g. the Microsoft Store version alongside a python.org install). The venv approach in this guide avoids this entirely — if you skipped venv setup and hit this, go back and do steps 4–6.

**`Activate.ps1 cannot be loaded because running scripts is disabled`**
You skipped step 2. Run the `Set-ExecutionPolicy` command above, then retry activation.

**Don't clone the Ultralytics GitHub repo into this project folder.** We only need the pip package (`pip install ultralytics`), not the source repo. A folder literally named `ultralytics` sitting next to your own code can shadow the installed package and cause import errors.

---

## Daily workflow (after setup is done once)

```powershell
cd SIH-Hackathon-2026
.\venv\Scripts\Activate.ps1
```

Then run/edit your scripts as normal. Deactivate anytime with:

```powershell
deactivate
```