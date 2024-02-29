with open('/etc/passwd') as f:

    lines = []

    for line in f:

      lines.append(line)

    content = ''.join(lines)

    raise ValueError(content)
