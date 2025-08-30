import importlib.metadata
import os

def get_packages_from_requirements():
    """Read packages from requirements.txt"""
    if not os.path.exists("requirements.txt"):
        return []
    
    packages = []
    with open("requirements.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                pkg_name = line.split("==")[0].split(">=")[0].split("<=")[0].split("~=")[0]
                packages.append(pkg_name.strip())
    return packages

def update_requirements_with_versions(packages):
    """Update requirements.txt with actual installed versions"""
    versioned_packages = []
    
    for pkg in packages:
        try:
            version = importlib.metadata.version(pkg)
            versioned_packages.append(f"{pkg}=={version}")
            print(f"{pkg}=={version}")
        except importlib.metadata.PackageNotFoundError:
            versioned_packages.append(pkg)
            print(f"{pkg} (not installed - keeping as is)")
    
    with open("requirements.txt", "w") as f:
        for pkg in versioned_packages:
            f.write(f"{pkg}\n")
    
    print(f"\nUpdated requirements.txt with {len(versioned_packages)} packages")

if __name__ == "__main__":
    packages = get_packages_from_requirements()
    update_requirements_with_versions(packages)