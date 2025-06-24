# Playwright Python Test Automation Framework

This is a simple test automation framework using Python + Playwright. It includes:

- Page Object Model
- Tests that can run in parallel
- Docker support
- .env-based configuration

## To run tests
```bash
pip install -r requirements.txt
python run_local.py
```

## To run using Docker
```bash
docker build -t playwright-tests .
docker run --rm playwright-tests
```

## To debug locally (headed mode)
```bash
python run_local.py --headed
```

## To run tests in parallel
```bash
python run_local.py -n 3
```