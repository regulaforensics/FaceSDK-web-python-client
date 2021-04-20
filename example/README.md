# Regula FaceSDK web API Python 3.5+ client

:warning: NOTE: for some systems `python3` and `pip3` commands should be used, instead of `python` and `pip`.

Requirements:
- installed python 3.5 or higher
- installed [pip](https://pip.pypa.io/en/stable/installing/)

Verify Python and pip versions:
```bash
python --version  
> Python 3.8.2
pip --version     
> pip 20.2.1 from /home/user/.local/lib/python3.8/site-packages/pip (python 3.8)
```

Cloning example:
```bash
git clone https://github.com/regulaforensics/FaceSDK-web-python-client.git
cd FaceSDK-web-python-client
```

Setup project and download dependencies:
```bash
pip install -e ./
```

### Running with local Regula FaceSDK web API installation

Assuming you have successfully launched instance, use next line command to run example:
```bash
cd example
python example.py

# If Regula FaceSDK web API is running not on localhost, specify host via env variable:
API_BASE_PATH="api_base_path" python example.py
```

### Output 
This sample generates next text output:
```text
-----------------------------------------------------------------
                         Matching Results                         
-----------------------------------------------------------------
pair(1, 2) similarity: 0.9995848536491394
pair(1, 3) similarity: 0.008510462939739227
pair(2, 3) similarity: 0.008510462939739227
-----------------------------------------------------------------
                         Detect Results                          
-----------------------------------------------------------------
detector_type: 3
landmark_type: 2
landmarks: [[588.0, 342.0], [735.0, 342.0], [668.0, 418.0], [607.0, 502.0], [725.0, 502.0]]
roi: [508.0, 267.0, 310.0, 310.0]
-----------------------------------------------------------------
```
