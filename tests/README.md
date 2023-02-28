#  Tools for Development

## Python
動作を確認する．
```sh
python tests/test.py
```

## Formatter
フォーマッターをかけて修正する．
```sh
isort {rsrs,tests,tools}/
black {rsrs,tests,tools}/
```

## Git
リモートリポジトリでマージしたら，ローカルで以下を実行してブランチを消しておく．
```sh
git fetch --prune
```
