run:
	@uvicorn \
		main:app \
		--host 0.0.0.0 \
		--port 8010 \
		--workers=1 \
		--reload
