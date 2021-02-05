#!/usr/bin/python3
import edgeos
import asyncio
import promethus_edgeos_metrics
import os


def main():

    # set these
    server = os.getenv('EDGEOS_SERVER')
    username = os.getenv('EDGEOS_USER')
    password = os.getenv('EDGEOS_PASS');
    subscriptions = ["interfaces", 'system-stats']

    # derive these
    auth_params = {'username': username, 'password': password}

    promethus_edgeos_metrics.start_server()

    websocket_exporter = edgeos.WS(
        server,
        auth_params,
        subscriptions,
        promethus_edgeos_metrics.register_edgeos_metrics
    )

    asyncio.run(websocket_exporter.collect_edgeos_metrics())


if __name__ == "__main__":
    main()