# calc-api-hands-on

シンプルな Azure Functions（Python 3.11）で乗算と除算を提供するサンプルプロジェクト。

## ローカルでの実行

1. Python 3.11 の仮想環境を作成して有効化

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. 依存関係をインストール

```powershell
pip install -r src\requirements.txt
pip install -r requirements-dev.txt
```

3. ローカルでの起動（Azure Functions Core Tools が必要）

```powershell
cd src
func start
```

4. ブラウザで確認

- http://localhost:7071/api/multiply?A=3&B=4
- http://localhost:7071/api/divide?A=10&B=2

## テスト

```powershell
# 仮想環境有効化後
pytest -q
```

## CI
- GitHub Actions ワークフローは `.github/workflows/ci.yml` に定義してあります。
- デプロイは上記ワークフロー内のテンプレートを参照し、Secrets（`AZURE_CREDENTIALS` 等）をセットして有効化してください。