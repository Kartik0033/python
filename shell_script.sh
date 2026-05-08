#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# Minimal, well-structured Bash script template
# - usage(), logging, arg parsing (getopts), main(), cleanup, trap

VERBOSE=0
OUTPUT=""

usage() {
  cat <<EOF
Usage: $(basename "$0") [-h] [-v] [-o output] [--] [args...]

Options:
  -h        Show this help and exit
  -v        Enable verbose logging
  -o FILE   Write output to FILE (defaults to stdout)

Example:
  $(basename "$0") -v -o result.txt input1 input2
EOF
}

log() {
  if [ "$VERBOSE" -ne 0 ]; then
    printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*"
  fi
}

cleanup() {
  # remove temp files or perform other cleanup tasks
  :
}
trap cleanup EXIT

parse_args() {
  OPTIND=1
  while getopts ":hvo:" opt; do
    case "$opt" in
      h) usage; exit 0 ;;
      v) VERBOSE=1 ;;
      o) OUTPUT="$OPTARG" ;;
      :) printf 'Option -%s requires an argument.\n' "$OPTARG" >&2; usage; exit 1 ;;
      \?) printf 'Invalid option: -%s\n' "$OPTARG" >&2; usage; exit 1 ;;
    esac
  done
  shift $((OPTIND-1))
  ARGS=("$@")
}

main() {
  parse_args "$@"
  log "Script started with args: ${ARGS[*]:-none}"

  # --- Core logic starts here ---
  # Example placeholder: echo inputs or write to output file
  if [ ${#ARGS[@]} -eq 0 ]; then
    echo "No positional arguments provided." 
  else
    if [ -n "$OUTPUT" ]; then
      printf '%s\n' "${ARGS[@]}" > "$OUTPUT"
      log "Wrote ${#ARGS[@]} items to $OUTPUT"
    else
      printf '%s\n' "${ARGS[@]}"
    fi
  fi
  # --- Core logic ends here ---

  log "Script finished"
}

# Execute main when script is run directly
if [ "${BASH_SOURCE[0]}" = "$0" ]; then
  main "$@"
fi

# End of shell_script.sh