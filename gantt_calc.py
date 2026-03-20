#!/usr/bin/env python3
"""Calcola i tempi per il diagramma Gantt CPU del server single-thread.
Usa dateFormat YYYY-MM-DD con date finte (1 giorno = 1 unità di tempo)."""

from datetime import datetime, timedelta

# Durate operazioni (in giorni, 1 giorno = 1 unità di tempo)
ACCEPT = 3
RECV = 5
ELABORA = 8
SEND = 5
CPU_TICK = 1

EPOCH = datetime(2000, 1, 1)

def d(offset):
    """Ritorna data come stringa YYYY-MM-DD."""
    return (EPOCH + timedelta(days=offset)).strftime("%Y-%m-%d")

# --- Client-1 timeline ---
c1 = {}
t = 0
c1["accept"] = (t, t + ACCEPT); t += ACCEPT
c1["recv"]   = (t, t + RECV);   t += RECV
c1["elab"]   = (t, t + ELABORA); t += ELABORA
c1["send"]   = (t, t + SEND);   t += SEND
c1_end = t

# --- Client-2 timeline ---
c2 = {}
c2_wait = (0, c1_end)
t = c1_end
c2["accept"] = (t, t + ACCEPT); t += ACCEPT
c2["recv"]   = (t, t + RECV);   t += RECV
c2["elab"]   = (t, t + ELABORA); t += ELABORA
c2["send"]   = (t, t + SEND);   t += SEND
c2_end = t

# --- CPU ticks ---
cpu_ticks = []
for client_ops in [c1, c2]:
    for op, (s, e) in client_ops.items():
        if op == "elab":
            cpu_ticks.append((s, e))
        else:
            cpu_ticks.append((s, s + CPU_TICK))
            cpu_ticks.append((e - CPU_TICK, e))

cpu_ticks.sort()
merged = []
for s, e in cpu_ticks:
    if merged and s <= merged[-1][1]:
        merged[-1] = (merged[-1][0], max(merged[-1][1], e))
    else:
        merged.append((s, e))

# --- Output Mermaid ---
print("``` mermaid")
print("%%{init: {'theme': 'dark', 'gantt': {'displayMode': 'compact'}} }%%")
print("gantt")
print("    dateFormat YYYY-MM-DD")
print("    axisFormat %j")
print("    title CPU del server (single-thread) — con utilizzo CPU")
print()
print("    section Client-1")
print(f"    accept() - I/O    :done, c1_accept, {d(c1['accept'][0])}, {ACCEPT}d")
print(f"    recv() - I/O      :done, c1_recv, after c1_accept, {RECV}d")
print(f"    elabora() - CPU   :active, c1_elab, after c1_recv, {ELABORA}d")
print(f"    send() - I/O      :done, c1_send, after c1_elab, {SEND}d")
print()
print("    section Client-2")
print(f"    in attesa          :crit, c2_wait, {d(0)}, {c1_end}d")
print(f"    accept() - I/O    :done, c2_accept, after c2_wait, {ACCEPT}d")
print(f"    recv() - I/O      :done, c2_recv, after c2_accept, {RECV}d")
print(f"    elabora() - CPU   :active, c2_elab, after c2_recv, {ELABORA}d")
print(f"    send() - I/O      :done, c2_send, after c2_elab, {SEND}d")
print()
print("    section CPU")
for i, (s, e) in enumerate(merged):
    print(f"    . :active, cp{i}, {d(s)}, {e - s}d")
print("```")

# Stats
total = c2_end
cpu = sum(e - s for s, e in merged)
print(f"\nCPU attiva: {cpu}/{total} ({cpu/total*100:.0f}%)")
print(f"CPU idle:   {total-cpu}/{total} ({(total-cpu)/total*100:.0f}%)")
