#!/usr/bin/env bash
# sync.sh — Faz commit de todas as alterações e envia para o GitHub.
# Uso: ./scripts/sync.sh ["mensagem de commit opcional"]

set -euo pipefail

ROOT_DIR="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
cd "$ROOT_DIR"

MSG="${1:-"chore: atualização automática via sync.sh [$(date '+%Y-%m-%d %H:%M')]"}"

echo "==> Adicionando alterações..."
git add .

if git diff --cached --quiet; then
  echo "Nenhuma alteração para commitar."
  exit 0
fi

echo "==> Criando commit: $MSG"
git commit -m "$MSG"

echo "==> Enviando para o GitHub..."
git push

echo "==> Pronto! Alterações publicadas."
