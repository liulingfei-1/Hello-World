# Hello World Collection

A curated set of minimal programs that print **"Hello, World"** in a variety of programming languages. This repository is useful for quick syntax lookups or verifying that a toolchain is configured correctly.

## Supported languages

- **C** – `HelloWorld.c`
- **C#** – `HelloWorld.cs`
- **C++** – `Helloworld.cpp`
- **Java** – `HelloWorld.java`
- **Python** – `HelloWorld.py`
- **Visual Basic** – `HelloWorld.vb`
- **TypeScript** – `Helloworld.ts`

## Running the examples
Each example is a single file that prints `Hello, World!` to standard output. Compile or interpret the file using the toolchain for that language:

### C
```bash
gcc HelloWorld.c -o hello && ./hello
```

### C#
```bash
csc HelloWorld.cs && ./HelloWorld.exe
```

### C++
```bash
g++ Helloworld.cpp -o hello && ./hello
```

### Java
```bash
javac HelloWorld.java && java HelloWorld
```

### Python
```bash
python HelloWorld.py
```

### Visual Basic
```bash
vbnc HelloWorld.vb && mono HelloWorld.exe
```

### TypeScript
```bash
tsc Helloworld.ts && node Helloworld.js
```

## Contributing

Feel free to submit pull requests that add new languages or improve existing examples.

## License

This project is licensed under the [MIT License](LICENSE).

