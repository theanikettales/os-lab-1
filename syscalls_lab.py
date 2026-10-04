import os
import sys
import subprocess

TEST_FILE = "test_file.txt"

print("=" * 50)
print("TASK 1: Create child process (os.fork)")
print("=" * 50)

pid = os.fork()

if pid == 0:
    # ---------- CHILD PROCESS ----------
    print("\n[CHILD] TASK 2: Process IDs")
    print(f"[CHILD] PID = {os.getpid()}, PPID = {os.getppid()}")

    print("\n[CHILD] TASK 4: Executing harmless Linux command (ls -l)")
    sys.stdout.flush()
    os.execvp("ls", ["ls", "-l"])  # replaces child image
    # code below never runs if exec succeeds
else:
    # ---------- PARENT PROCESS ----------
    print(f"\n[PARENT] TASK 2: PID = {os.getpid()}, Child PID = {pid}")

    print("\n[PARENT] TASK 3: Waiting for child to complete...")
    child_pid, status = os.waitpid(pid, 0)
    print(f"[PARENT] Child {child_pid} finished, exit status = {os.WEXITSTATUS(status)}")

    # ---------- TASK 5: File operations ----------
    print("\nTASK 5: File create/write/read/close")
    fd = os.open(TEST_FILE, os.O_CREAT | os.O_WRONLY | os.O_TRUNC, 0o644)
    os.write(fd, b"Hello from system call write()\n")
    os.close(fd)

    fd = os.open(TEST_FILE, os.O_RDONLY)
    data = os.read(fd, 100)
    os.close(fd)
    print("Read back:", data.decode().strip())

    # ---------- TASK 6: Device / proc interfaces ----------
    print("\nTASK 6: Inspect /dev/null, /dev/zero, /proc")
    with open("/dev/null", "wb") as f:
        f.write(b"discarded data")
    print("/dev/null  -> write succeeded, data discarded")

    with open("/dev/zero", "rb") as f:
        zeros = f.read(8)
    print("/dev/zero  -> read 8 bytes:", zeros)

    with open("/proc/self/status") as f:
        for _ in range(3):
            print("/proc/self/status ->", f.readline().strip())

    # ---------- TASK 7: Error handling ----------
    print("\nTASK 7: Error handling")
    try:
        open("/invalid/path/file.txt", "r")
    except FileNotFoundError as e:
        print(f"Error: File not found -> {e}")
    except PermissionError as e:
        print(f"Error: Permission denied -> {e}")
    except OSError as e:
        print(f"Error: OS error [{e.errno}] -> {e.strerror}")

    try:
        os.open("/nonexistent_dir/x.txt", os.O_RDONLY)
    except OSError as e:
        print(f"Failed file operation: errno={e.errno}, message={e.strerror}")

    # ---------- TASK 8: Evidence ----------
    print("\nTASK 8: Evidence summary")
    print(f"Process   : parent PID {os.getpid()}, child PID {pid}")
    print(f"File      : {TEST_FILE} ({os.path.getsize(TEST_FILE)} bytes)")
    print("Device    : /dev/null, /dev/zero, /proc/self/status accessed")
    print("Errors    : handled with try/except")
    os.remove(TEST_FILE)
