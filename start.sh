#!/bin/bash
# Fios MJ - Start Script
export JAVA_HOME="/home/linuxbrew/.linuxbrew/opt/openjdk"
export PATH="$JAVA_HOME/bin:$PATH"

JAR="/data/.openclaw/workspace/fiosmj-app/target/fiosmj-app-1.0.0.jar"
LOG="/data/.openclaw/workspace/fiosmj-app/app.log"
PID_FILE="/data/.openclaw/workspace/fiosmj-app/app.pid"

case "$1" in
  start)
    if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
      echo "Fios MJ já está rodando (PID $(cat $PID_FILE))"
      exit 0
    fi
    echo "Iniciando Fios MJ..."
    nohup java -jar "$JAR" > "$LOG" 2>&1 &
    echo $! > "$PID_FILE"
    echo "Fios MJ iniciado (PID $!)"
    ;;
  stop)
    if [ -f "$PID_FILE" ]; then
      kill $(cat "$PID_FILE") 2>/dev/null
      rm -f "$PID_FILE"
      echo "Fios MJ parado"
    else
      echo "Fios MJ não está rodando"
    fi
    ;;
  restart)
    $0 stop
    sleep 2
    $0 start
    ;;
  status)
    if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
      echo "Fios MJ rodando (PID $(cat $PID_FILE))"
    else
      echo "Fios MJ parado"
      rm -f "$PID_FILE"
    fi
    ;;
  *)
    echo "Uso: $0 {start|stop|restart|status}"
    ;;
esac
