{
    description = "Python Development Environment";

    inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    outputs = { self, nixpkgs }:
        let 
        system = "x86_64-linux";
        pkgs = import nixpkgs { inherit system; };
    in {
        devShells.${system}.default = pkgs.mkShell {
            buildInputs = [
                pkgs.pyright
                pkgs.python3
            ];
            shellHook = ''
                echo "Entwicklungsumgebung für Python gestartet!"
                '';
        };
    };
}
