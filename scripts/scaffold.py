#!/usr/bin/env python3
import subprocess
import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Scaffold a new Stylus project")
    parser.add_argument("name", help="Name of the project")
    args = parser.parse_args()

    project_name = args.name

    print(f"🚀 Initializing Stylus project: {project_name}...")

    # 1. Run cargo stylus new
    try:
        subprocess.check_call(["cargo", "stylus", "new", project_name])
    except subprocess.CalledProcessError:
        print("❌ Failed to create project. Ensure 'cargo-stylus' is installed.")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ 'cargo' not found in PATH.")
        sys.exit(1)

    project_path = os.path.join(os.getcwd(), project_name)
    cargo_toml_path = os.path.join(project_path, "Cargo.toml")

    # 2. Modify Cargo.toml
    print("🛠️  Configuring Cargo.toml for optimization and dependencies...")
    
    with open(cargo_toml_path, "a") as f:
        # Optimization profile
        f.write("\n\n[profile.release]\n")
        f.write("codegen-units = 1\n")
        f.write("strip = true\n")
        f.write("lto = true\n")
        f.write("panic = \"abort\"\n")
        f.write("opt-level = \"z\"\n")
        
        # Dependencies logic could be more sophisticated (parsing toml), 
        # but appending is safe for a fresh project.
        f.write("\n[dependencies]\n")
        f.write("stylus-sdk = \"0.6.0\"\n")
        f.write("alloy-sol-types = \"0.7.0\"\n")
        
        f.write("\n[dev-dependencies]\n")
        f.write("motsu = \"0.1\"\n") 

    print("✅ Project scaffolded successfully!")
    print(f"👉 cd {project_name}")
    print("👉 cargo stylus check")

if __name__ == "__main__":
    main()
