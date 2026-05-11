#!/usr/bin/env python3
import os
import sys
import subprocess

MAX_SIZE_KB = 24

def get_wasm_size(wasm_path):
    size_bytes = os.path.getsize(wasm_path)
    return size_bytes / 1024

def main():
    print("🔍 Searching for WASM files in target/wasm32-unknown-unknown/release/...")
    
    target_dir = os.path.join(os.getcwd(), "target", "wasm32-unknown-unknown", "release")
    
    if not os.path.exists(target_dir):
        print(f"❌ Target directory not found: {target_dir}")
        print("   Run 'cargo stylus check' or 'cargo build --release --target wasm32-unknown-unknown' first.")
        sys.exit(1)

    wasm_files = [f for f in os.listdir(target_dir) if f.endswith(".wasm")]
    
    if not wasm_files:
        print("❌ No WASM files found.")
        sys.exit(1)

    any_fail = False

    for wasm_file in wasm_files:
        path = os.path.join(target_dir, wasm_file)
        size_kb = get_wasm_size(path)
        
        if size_kb > MAX_SIZE_KB:
            print(f"⚠️  {wasm_file}: {size_kb:.2f}KB (EXCEEDS {MAX_SIZE_KB}KB)")
            any_fail = True
        else:
            print(f"✅ {wasm_file}: {size_kb:.2f}KB")

    if any_fail:
        print("\n❌ One or more files exceed the 24KB limit.")
        print("   Suggestions:")
        print("   1. Verify Cargo.toml has [profile.release] opt-level = 'z'")
        print("   2. Remove unused dependencies.")
        print("   3. Avoid heavy crates like 'serde' with default features.")
        sys.exit(1)
    else:
        print("\n🎉 All contracts are within size limits!")

if __name__ == "__main__":
    main()
