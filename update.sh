#!/usr/bin/env bash
# Update this kit to the latest version from github.com/Mahanaicoach/funnel-spy.
# Works whether you cloned the original repo or your own fork. Your own commits
# are kept: git merges the update into them.
#
#   bash update.sh
set -euo pipefail

UPSTREAM="https://github.com/Mahanaicoach/funnel-spy.git"
BRANCH="main"

KIT_DIR="$(cd "$(dirname "$0")" && pwd -P)"
cd "$KIT_DIR"

# A ZIP download has no git history. Check the top level too, so a copy inside
# another repo (for example a git-tracked ~/.claude) is never merged into it.
if [ "$(git rev-parse --show-toplevel 2>/dev/null)" != "$KIT_DIR" ]; then
  echo "This folder is not a git clone of the kit, so it can't update itself."
  echo "Clone it again: git clone $UPSTREAM"
  exit 1
fi

if ! git diff --quiet HEAD --; then
  echo "You have uncommitted changes. Save them with 'git stash' (or commit them), then run this again."
  exit 1
fi

git remote get-url upstream >/dev/null 2>&1 || git remote add upstream "$UPSTREAM"
git fetch --quiet upstream "$BRANCH"

if ! git merge-base HEAD "upstream/$BRANCH" >/dev/null; then
  echo "This copy shares no history with the original (it was made with 'Use this template',"
  echo "or it is a shallow clone), so git can't merge updates into it."
  echo "See what changed: https://github.com/Mahanaicoach/funnel-spy/commits/$BRANCH"
  exit 1
fi

BEFORE="$(git rev-parse HEAD)"
if ! git merge --no-edit "upstream/$BRANCH"; then
  echo
  echo "The update conflicts with your own changes in the files listed above."
  echo "Fix them, then run: git add -A && git commit --no-edit"
  echo "Or undo the update: git merge --abort"
  exit 1
fi

if [ "$BEFORE" = "$(git rev-parse HEAD)" ]; then
  echo "Already up to date."
else
  echo "Updated. What's new:"
  git log --oneline --no-merges -n 20 "$BEFORE..HEAD"
  if ! git remote get-url origin 2>/dev/null | grep -qi "mahanaicoach/funnel-spy"; then
    echo "Your fork on GitHub is still on the old version. Run 'git push' to update it too."
  fi
fi

# Claude Code users copied the skill folder into ~/.claude/skills. Refresh that copy.
SKILL_COPY="$HOME/.claude/skills/funnel-spy"
if [ -d "$SKILL_COPY" ] && [ "$(cd "$SKILL_COPY" && pwd -P)" != "$KIT_DIR/funnel-spy" ]; then
  cp -R "funnel-spy/." "$SKILL_COPY/"
  echo "Refreshed your installed skill in $SKILL_COPY"
fi
if [ -f "$HOME/.claude/commands/funnel-spy.md" ]; then
  cp "commands/funnel-spy.md" "$HOME/.claude/commands/funnel-spy.md"
  echo "Refreshed the /funnel-spy command"
fi
echo "Using the Claude desktop app? Download funnel-spy.skill again and click Save skill."
