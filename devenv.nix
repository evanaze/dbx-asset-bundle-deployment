{pkgs, ...}: {
  # https://devenv.sh/packages/
  packages = with pkgs; [
    python312Full
    databricks-cli
    python312Packages.pytest
    python312Packages.databricks-sdk
  ];

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    package = pkgs.python312Full;
  };

  # https://devenv.sh/scripts/
  processes.nb.exec = "jupyter notebook";

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    git --version | grep --color=auto "${pkgs.git.version}"
  '';

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}
