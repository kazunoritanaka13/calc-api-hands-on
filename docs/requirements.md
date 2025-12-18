# 機能要件

## 概要
- 本プロジェクトは Azure Functions (Consumption Plan) を用いて、2つの HTTP API を提供する。
  - 乗算 API: `/multiply`
  - 除算 API: `/divide`
- リクエストは GET メソッドで受け取り、クエリストリングとして `A` と `B`（大文字）を整数で受け取る。
- レスポンスは JSON 形式で `result` を返す。

## デプロイ環境
- リージョン: 東日本 (Japan East)
- プラン: Azure Functions - Consumption Plan
- ランタイム: Python 3.11
- `FUNCTIONS_WORKER_RUNTIME=python`
- `FUNCTIONS_EXTENSION_VERSION=~4`

## API 仕様
- 共通項目
  - HTTP メソッド: `GET`
  - クエリパラメータ: `A` (必須, 整数), `B` (必須, 整数)
  - 出力: `application/json`
  - 出力フォーマット: `{ "result": <整数> }`
  - 認証: 不要（パブリック）

- `/multiply`
  - 機能: `A * B` を計算して返す
  - 例: `GET /multiply?A=3&B=4` -> `{ "result": 12 }`

- `/divide`
  - 機能: `A / B` を計算して返す（整数割り算の取り扱いは下記参照）
  - 例: `GET /divide?A=10&B=2` -> `{ "result": 5 }`
  - 前提: 本仕様では `B` が 0 とならないことを想定する（入力検証は実装しない）。

## 入力検証・エラーハンドリング
- 今回の実装方針として、`A`,`B` はクライアントが整数で正しく送信することを前提とする。
- 不正入力（非数、未指定、`B==0`）の取り扱いは今回の対象外とする（挙動は未定義）。

## 依存関係
- `azure-functions`（Azure Functions Python ランタイム用ライブラリ）
- その他は実装時に `requirements.txt` に記載する。

## ローカル開発手順（要約）
1. Python 3.11 の仮想環境を作成・有効化
2. `pip install -r requirements.txt`
3. `func start` でローカル起動（Azure Functions Core Tools v4 を使用）

## CI / デプロイ
- GitHub Actions を想定
  - テスト: `pytest` を実行して単体テストを確認すること
  - デプロイ: `azure/functions-action` 等を使い、Secrets（Publish Profile または Service Principal）を使用して Function App にデプロイする
- リモートビルドを有効にする場合、アプリ設定に `SCM_DO_BUILD_DURING_DEPLOYMENT=true` を設定すること

## 受け入れ基準
- ブラウザで以下のリクエストを入力して期待値が JSON で返ること
  - `/multiply?A=3&B=4` -> `{ "result": 12 }`
  - `/divide?A=10&B=2` -> `{ "result": 5 }`
- 単体テストが `pytest` で実行され、主要ロジック（乗算・除算）のテストが通ること

## 実装メモ（簡易）
- 各 Function は `__init__.py` 内で HTTP トリガーを受け取り、クエリ `A`, `B` を取得して演算し JSON を返す
- `host.json`、`function.json` を標準的に用意する
