FROM python:3.13.2-alpine

ARG USER_ID
ARG GROUP_ID

RUN addgroup -g ${GROUP_ID} -S mygroup || \
    adduser --system -G "$(getent group ${GROUP_ID} | cut -d: -f1)" --uid ${USER_ID} me

USER me
