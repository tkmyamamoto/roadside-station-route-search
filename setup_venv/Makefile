PYTHON_VERSION:= 3.7
PYTORCH_VERSION:= 1.12.1
TORCH_VISION_VERSION:= 0.13.1
CUDA_VERSION:= 11.3

.PHONY: all clean showenv

all: showenv virtualenv.done requirements.done

showenv:
	@echo "=================================================="
	@echo "- PYTHON=$(shell command -v python3)"
	@echo "- PYTHON_VERSION=$(PYTHON_VERSION)"
	@echo "- PYTORCH_VERSION=$(PYTORCH_VERSION)"
	@echo "- TORCH_VISION_VERSION=$(TORCH_VISION_VERSION)"
	@echo "- CUDA_VERSION=$(CUDA_VERSION)"
	@echo "=================================================="

virtualenv.done: showenv
	test -d venv || $(shell command -v python3) -m venv rsrs_env
	. rsrs_env/bin/activate && pip install -U pip wheel setuptools
	touch virtualenv.done

requirements.done: virtualenv.done
	. rsrs_env/bin/activate && pip install -r requirements.txt
	touch requirements.done

clean:
	rm -fr venv *.done
	find -iname "*.pyc" -delete
