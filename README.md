# Final-Project

## Setup

Obtain an [AlphaVantage API Key](https://www.alphavantage.co/support/#api-key). A normal key should be fine, but alternatively you can use one of the prof's "premium" keys.

Create a virtual environment:

```sh
conda create -n final-project-env python=3.10
```

```sh
conda activate final-project-env
```

Install third-party packages:

```sh
pip install -r requirements.txt
```

## Usage

Run the report:

```sh
python app/final-project.py

python -m app.final
```

## Testing

Run tests:

```sh
pytest
```