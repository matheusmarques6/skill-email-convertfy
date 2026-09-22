#!/usr/bin/env bash
# Recria o que nao e versionado: o symlink do vault e os clones de vendor/.
# Uso:
#   ./scripts/setup.sh
#   CONVERTFY_VAULT="/caminho/para/Admin Convertfy/Emails" ./scripts/setup.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

VAULT_REPO="https://github.com/matheusmarques6/all-for-eficiencia"
VAULT_SUBPATH="Admin Convertfy/Emails"

# --- vault ---------------------------------------------------------------
if [ -n "${CONVERTFY_VAULT:-}" ]; then
  VAULT_TARGET="$CONVERTFY_VAULT"
else
  VAULT_CLONE="${CONVERTFY_VAULT_CLONE:-$HOME/all-for-eficiencia}"
  if [ -d "$VAULT_CLONE/.git" ]; then
    echo "vault: clone ja existe em $VAULT_CLONE"
  else
    echo "vault: clonando $VAULT_REPO -> $VAULT_CLONE"
    git clone --depth 1 "$VAULT_REPO" "$VAULT_CLONE"
  fi
  VAULT_TARGET="$VAULT_CLONE/$VAULT_SUBPATH"
fi

if [ -d "$VAULT_TARGET" ]; then
  ln -sfn "$VAULT_TARGET" vault
  echo "vault: symlink -> $VAULT_TARGET"
else
  echo "vault: ERRO, caminho nao encontrado: $VAULT_TARGET" >&2
  echo "       defina CONVERTFY_VAULT com o caminho da pasta Emails." >&2
  exit 1
fi

# --- vendor --------------------------------------------------------------
# Somente leitura. Nunca editar, nunca copiar para skills/. Ver NOTICE.md.
REPOS="
pbakaus/impeccable
Leonxlnx/taste-skill
emilkowalski/skills
CosmoBlk/email-marketing-bible
808enzo/chappie
davidharttx/email-campaign-skill
framix-team/skill-email-html-mjml
EmailBoutique-Digital-Inc/email-html-qa-skill
Join-Ground-AI/Ground-Retention-Skills
jayreis/prescott-amelia-agents
thatrebeccarae/claude-marketing
olivalcf/klaviyo-audit-agent-skill
"

mkdir -p vendor
for repo in $REPOS; do
  name="${repo##*/}"
  if [ -d "vendor/$name/.git" ]; then
    echo "vendor: $name ja presente"
  else
    echo "vendor: clonando $repo"
    git clone --depth 1 --quiet "https://github.com/$repo.git" "vendor/$name" \
      || echo "vendor: FALHOU $repo" >&2
  fi
done

echo
echo "pronto. leia CLAUDE.md antes de escrever skill."
