{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "J2IwI1wyY7gV",
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "<p style='text-align: left; color: #a0d2eb; font-size: 1.5rem; font-weight:bold;'>[2024 직무연수]</p>\n",
    "\n",
    "<h1 style='text-align: center; color: #8458B3; font-size: 4rem; font-weight:bold;'>Python을 이용한 해양데이터 활용 실습(1)</h1>\n",
    "\n",
    "<h2 style='text-align: center; color: #a28089; font-size: 3.5rem; font-style:italic;'>\"우리나라에서 가장 깊은 바다는 어디?\"</h2>\n",
    "<h3 style='text-align: center; color: #D0BDF4; font-size: 3rem; font-weight:bold; padding-top:3.5em;'>송태윤</h3>\n",
    "<p style='text-align: center; color: #a0d2eb; font-size: 1.5rem; font-weight:bold; margin:0.5em 0 1em 0;'>해봄데이터(주)</p>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "OpMrhE0BYmBO",
    "lang": "en",
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "<h3 style='text-align: center; color:#D0BDF4; font-size:5rem; font-weight:bold; line-height:5rem; margin-bottom:5rem;'>GOAL</h3>\n",
    "    \n",
    "<div style='padding-left: 3rem;margin:auto; width:80%; color:#a28089; font-size: 3rem;font-weight:bold;'>\n",
    "<ol style='line-height:5rem;'>\n",
    "    <li><span style='font-style:bold;'>해양관측데이터란 무엇이고 수집하는 방법을 알 수 있다.</span></li>\n",
    "    <li><span style='font-style:bold;'>python을 이용하여 우리나라 해저지형도를 만들 수 있다.</span></li>\n",
    "    <li>OpenAPI를 이용하여 실시간 해양정보를 활용할 수 있다.</li>\n",
    "</ol>\n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "K4jvNUf9yp9y",
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "<h3 style='text-align: center; color:#D0BDF4; font-size:5rem; font-weight:bold; line-height:5rem; margin-bottom:5rem;'>목차</h3>\n",
    "\n",
    "<div style='padding-left:3rem; margin:auto; width:70%; color:#a28089 ; font-size: 3rem; font-weight:bold;'>\n",
    "    <ol style='line-height:3rem;'>\n",
    "        <li>해양관측데이터와 제공 사이트</li>\n",
    "        <li>Google Earth Engine 이란?</li>\n",
    "        <li>Earth Engine Python API 이용을 위한 Setup</li>\n",
    "        <li>맵(Map) 시각화</li>\n",
    "    </ol>\n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "grSwqbJOhjQG",
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "<h3 style=\"font-weight:bold; font-size:3rem;line-height:2rem; color:#a28089;\">1. 해양관측데이터와 제공 사이트</h3>\n",
    "<div style='margin:auto; width:80%; margin-top:3rem; display:flex'>\n",
    "<img style='width:300px;height:300px;object-fit:cover; margin:5px' src=\"https://github.com/Marino89/teacher_training/blob/main/image/oceanObs2021-morris-f3.jpg?raw=true\">\n",
    "<img style='width:auto;height:300px;object-fit:cover; margin:5px' src=\"https://github.com/Marino89/teacher_training/blob/main/image/global-ocean-observing-system-for-climate.jpg?raw=true\">\n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Ry3xN3Tkp3G3",
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "<h6 style='color:#a28089; font-size:1.5rem; font-weight:bold; line-height:2rem;'>1. 해양관측데이터와 제공 사이트</h6>\n",
    "<div style='margin:auto; width:90%; margin-top:1.5rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>해외기관</p>\n",
    "    <ul style='font-size:2rem;line-height:3rem; margin-top:0.2rem'>\n",
    "        <li><a href='https://www.ncei.noaa.gov/products/world-ocean-database'>WOD(World Ocean Database)</a>: WOD는 해양 데이터의 글로벌 데이터베이스로, 해양과학 연구자들이 사용할 수 있는 다양한 해양관측자료(수온, 염분, 영얌염류 등)를 제공</li>\n",
    "        <li><a href='https://www.bodc.ac.uk/'>BODC(British Oceanographic Data Center</a>: BODC는 영국의 해양데이터 및 정보 센터로, 해양 데이터를 수집하고 보존하며 배포</li>\n",
    "        <li><a href='https://www.copernicus.eu/en'>Copernicus</a>:Copernicus는 유럽연합의 지구 관측 프로그램으로, 해양, 대기, 육지 및 기후 변화를 포함한 다양한 환경 데이터를 제공하며 해양 데이터 분야에서는 해양 관측 및 예측 서비스를 통해 해양 상태에 대한 실시간 정보를 제공</li>\n",
    "    </ul>           \n",
    "</div>\n",
    "\n",
    "<div style='margin:auto; width:90%; margin-top:1.5rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>국내기관</p>\n",
    "    <ul style='font-size:2rem;line-height:3rem; margin:0.2rem;'>\n",
    "        <li><a href='https://www.khoa.go.kr/'>국립해양조사원</a></li>\n",
    "        <li><a href='https://www.weather.go.kr/w/index.do'>기상청</a></li>\n",
    "        <li><a href='https://www.nifs.go.kr/main.do'>국립수산과학원</a></li>\n",
    "        <li><a href='https://www.koem.or.kr/site/koem/main.do'>해양환경공단</a></li>\n",
    "        <li><a href='https://joiss.kr/joiss/'>JOISS</a></li>\n",
    "    </ul>           \n",
    "</div>\n",
    "\n",
    "<div style='margin:auto; width:90%; margin-top:1.5rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>주제별 웹사이트</p>\n",
    "    <ul style='font-size:2rem;line-height:3rem; margin:0.2rem'>\n",
    "        <li>수심: <a href='https://www.gebco.net/'>GEBCO (The General Bathymetric Chart of the Oceans)</a></li>\n",
    "        <li>해양경계:<a href='https://www.marineregions.org/eez.php'>Marineregion.org</a></li>\n",
    "        <li>지구관측DB:<a href='https://earthengine.google.com/'>Google Earth Engine(GEE)</a></li>\n",
    "    </ul>           \n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "6_aWU8wWYRK6",
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "<h3 style='color:#a28089; font-size:3rem; font-weight:bold; line-height:2rem;'>2. Google Earth Engine와 GEEMAP</h3>\n",
    "<div style='margin:auto; width:90%; margin-top:3rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>Google Earth Engine 이란?</p>\n",
    "    <ul style='font-size:2rem;line-height:3rem'>\n",
    "        <li>GEE는 <span style='color:#d0bdf4; font-style:bold;'>지리공간데이터 분석 및 시각화 플랫폼</span>으로써 위성영상 및 40년 이상의 지구관측이미지 데이터와 함께 학술, 영리 및 비영리, 공공에 서비스</li>\n",
    "        <li>특징: 개방 데이터 카탈로그, 병렬계산 컴퓨팅 인프라, 지리공간API, 인터랙티브 앱 서버 제공</li>\n",
    "    </ul>           \n",
    "</div>\n",
    "<div style='justify-content:center; width:70%; margin:auto; margin-top:3rem;'>\n",
    "    <blockquote>\n",
    "        <p style='font-size:2rem; font-style:bold;'><em>Google Earth와 무엇이 다른가?</em></p>\n",
    "        <p style='font-size:1.5rem; '>구글어스는 가상지구본을 통한 셰계 탐색 도구인 반면, 어스엔진은 지리공간데이터 분석 도구임</p>\n",
    "    </blockquote>\n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "_hzbCt6Iyp90",
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "<h6 style='color:#a28089; font-size:1.5rem; font-weight:bold; line-height:2rem;'>2. Google Earth Engine와 GEEMAP</h6>\n",
    "\n",
    "<div style='margin:auto; width:90%; margin-top:1rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>Google Earth Engine 기초</p>\n",
    "    <div style=\"float:right; margin-right:5rem ; margin-left:0; width:70%\">\n",
    "        <img src='https://github.com/Marino89/teacher_training/blob/main/image/Code_editor_diagram.png?raw=true'>\n",
    "        <figcaption style='text-align:center; font-size:2rem;margin-bottom:3rem;padding-bottom:2rem'>Javascript를 지원하는 GEE의 코드편집기 (출처:Google Earth Engine)</figcaption>\n",
    "    </div>\n",
    "    <div style=\"width:30%; padding-top:2rem ; font-size:2rem;margin-top-bottom:1rem 0rem;\">\n",
    "        <ul style='font-size:2rem; line-height:3rem'>\n",
    "            <li><a href='https://developers.google.com/earth-engine/guides/playground'>GEE Code Editor</a></li>\n",
    "            <li><a href='https://developers.google.com/earth-engine/datasets'>GEE Data Catalog</a></li>\n",
    "            <li><a href='https://earthengine.google.com/timelapse/'>타임랩스(Timelapse)</a></li>\n",
    "        </ul>\n",
    "    </div>\n",
    "    \n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "XpVFfwSgyp90",
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "<h6 style='color:#a28089; font-size:1.5rem; font-weight:bold; line-height:2rem;'>2. Google Earth Engine와 GEEMAP</h6>\n",
    "<div style='margin:auto; width:90%; margin-top:3rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>GEE의 대표적인 객체들(데이터 구조)</p>\n",
    "    <ul style='font-size:2rem;line-height:3rem'>\n",
    "        <li><code>Image</code></li>\n",
    "            <ul>\n",
    "                <li>GEE에서 <code>Image</code>는 위성 이미지, 토지 피복, 온도, 고도 등의 정보를 나타내는 래스터 데이터를 의미합니다. <code>Image</code>는 픽셀의 그리드로 구성되어 있으며, 각 픽셀은 특정 위치에 대한 값을 포함합니다. <code>Image</code>는 여러 밴드를 가질 수 있으며, 각 밴드는 동일한 위치에서 다른 유형의 데이터나 관측값을 저장할 수 있습니다.</li>\n",
    "                <li>예: <code>Image</code>는 특정 지역의 위성 사진을 나타낼 수 있으며, 각기 다른 밴드는 가시광선, 적외선 등의 스펙트럼 정보를 보여줄 수 있습니다.</li>\n",
    "            </ul>\n",
    "        <li><code>ImageCollection</code></li>\n",
    "        <li><code>Geometry</code></li>\n",
    "             <ul>\n",
    "                 <li>GEE에서 `Geometry`는 지구 표면상의 형태와 위치를 정의하는 데 사용됩니다. 이는 점(point), 선(line), 또는 폴리곤(polygon)일 수 있습니다. Geometry는 분석을 위한 관심 지역이나 공간 필터링을 위한 경계를 지정하는 데 필수적입니다.</li>\n",
    "                  <li>예: `Geometry`는 도시의 경계(폴리곤), 강의 경로(선), 기상 관측소의 위치(점)를 정의할 수 있습니다.</li>\n",
    "              </ul>\n",
    "         <li><code>Feature</code></li>\n",
    "               <ul>\n",
    "                  <li>`Feature`는 공간 정보(`Geometry`로 정의됨)와 추가 속성 또는 특성을 결합한 것입니다. 기본적으로, 이는 설명적인 정보를 동반한 `Geometry`입니다. Features는 공간 데이터와 관련된 메타데이터를 저장하고 분석하는 데 유용합니다.</li>\n",
    "                  <li>예: `Feature`는 특정 숲 지역(`Geometry`로서의 폴리곤)과 숲의 유형, 나이, 수관 밀도와 같은 속성을 나타낼 수 있습니다.</li>\n",
    "            </ul>\n",
    "        <li><code>FeatureCollection</code></li>\n",
    "    </ul>           \n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "xpwjHwJJBZe4",
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "<h6 style='color:#a28089; font-size:1.5rem; font-weight:bold; line-height:2rem;'>2. Google Earth Engine와 GEEMAP</h6>\n",
    "<div style='margin:auto; width:90%; margin-top:3rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>GEEMP 패키지</p>\n",
    "    <ul style='font-size:2rem;'>\n",
    "        <li><a href='https://geemap.org/'>GEEMP</a></li>\n",
    "    </ul>           \n",
    "</div>\n",
    "<div style='margin:auto; width:80%;'>\n",
    "    <img src='https://www.kdnuggets.com/wp-content/uploads/anello_geospatial_data_analysis_geemap_1.png'>\n",
    "    <figcaption style='text-align:center; font-size:2rem;margin-bottom:3rem;padding-bottom:2rem'>GEEMAP은 GEE와 파이썬을 연결해주는 패키지</figcaption>\n",
    "</div>\n",
    "\n",
    "<h6 style='font-size:1.5rem;'>참고문헌</h6>\n",
    "   <ol style='font-size:1.5rem;'>\n",
    "      <li>\n",
    "         <p>Wu, Q., <cite>geemap: A Python package for interactive mapping with Google Earth Engine. The Journal of Open Source Software</cite>, 5(51), 2305. <a href='https://doi.org/10.21105/joss.02305'>https://doi.org/10.21105/joss.02305</p>\n",
    "    </li>\n",
    "   </ol>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "LAZiVi13zTE7",
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "<h3 style='color:#a28089; font-size:3rem; font-weight:bold; line-height:2rem;'>3. Earth Engine Python API 이용을 위한 Setup</h3>\n",
    "<div style='margin:auto; width:90%; margin-top:3rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>API 불러오기(import)와 토큰 인증</p>\n",
    "    <ul style='font-size:2rem;line-height:3rem'>\n",
    "        <li><em>EE API</em>는 <em>Colab</em>에 기본 설치되므로 불러오기와 인증단계만을 요구함. <em>Colab</em> 커널을 재시작하거나 <em>Colab</em> 가상머신이 비활성화로 인해 재시작하는 경우에도 이 단계를 거쳐야 함.</li>\n",
    "    </ul>           \n",
    "</div>\n",
    "<div style='margin:auto; width:90%; margin-top:3rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>인증(Authenticate)과 (초기화)Initialize</p>\n",
    "    <ul style='font-size:2rem; line-height:3rem'>\n",
    "        <li><code>ee.Authenticate</code> 함수 실행: Earth Engine 서버 접속을 승인하기 위함</li>\n",
    "        <li><code>ee.Initialize</code> : 초기화</li>\n",
    "        <li>이 단계를 거치면 Earth Engine에 Google 계정 액세스 권한을 부여하라는 메시지가 표시되며 셀에 인쇄된 지침을 따름</li>\n",
    "    </ul>           \n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "id": "65RChERMzQHZ",
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [],
   "source": [
    "# Earth Engine API 불러오기\n",
    "import ee\n",
    "\n",
    "# Trigger the authentication flow.\n",
    "ee.Authenticate()\n",
    "\n",
    "# Initialize the library.\n",
    "ee.Initialize(project='ee-haebom')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "fDLAqiNWeD6t",
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "<h3 style='color:#a28089; font-size:3rem; font-weight:bold; line-height:2rem;'>4. 맵(Map) 시각화</h3>\n",
    "<div style='margin:auto; width:90%; margin-top:3rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>인터랙티브 맵(Interactive map)</p>\n",
    "    <ul style='font-size:2rem;line-height:3rem'>\n",
    "        <li><a href='https://github.com/gee-community/geemap'>GEEMAP</a> 라이브러리를 사용하여 <code>ee.Image</code> 객체를 대화형 <a href='https://github.com/jupyter-widgets/ipyleaflet'>ipyleaflet</a> 맵에 시각화한다.</li>\n",
    "        <li>[실습] GEE API를 이용해서 한반도 상공의 Landsat 위성영상 찾기</li>\n",
    "    </ul>           \n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "id": "iia8D1yvXCts",
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [],
   "source": [
    "# geemap 리이브러리 설치 및 업데이트\n",
    "%pip install -U geemap\n",
    "\n",
    "# geemap 라이브러리 블러오기\n",
    "import geemap\n",
    "import geemap.colormaps as cm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "TN3EO7ztZV4C",
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [],
   "source": [
    "# 부산의 좌표(128.9697, 35.1796)를 Geometry 포인트로 생성하여 관심지역(roi: region of interest)으로 설정한다.\n",
    "roi = ee.Geometry.Point(128.9697, 35.1796)\n",
    "\n",
    "# GEE 카탈로그에 있는 Landsat-9 콜력션(LANDSAT/LC09/C02/T1_TOA) 이용\n",
    "# 날짜로 영상 필터(filterDate) : 2022-01-01와 2022-12-01 사이\n",
    "# 지역(영역) 필터(filterBounds)\n",
    "# 구름 필터\n",
    "landsat9 = ee.ImageCollection('LANDSAT/LC09/C02/T1_TOA')\n",
    "l9filter= landsat9.filterDate(\n",
    "    '2022-01-01', '2022-12-01').filterBounds(roi).filter(ee.Filter.lt('CLOUD_COVER', 10))\n",
    "\n",
    "# True Color 영상합성을 위해 RGB밴드(B4, B3, B2) 선택 후 이들 영상 중 첫 영상(first)을 선택하여 trueColor432 변수에 할당\n",
    "trueColor432 = l9filter.select(['B4', 'B3', 'B2']).first();\n",
    "# 시각화\n",
    "trueColor432Vis = {\n",
    "  'min': 0.0,\n",
    "  'max': 0.4,\n",
    "};\n",
    "# Map 인스턴스 생성\n",
    "m = geemap.Map()\n",
    "# 관심지역(roi)으로 map 이동 및 확대(8)\n",
    "m.centerObject(roi, 8)\n",
    "# trueColor432 영상을 레이어로 추가\n",
    "m.add_layer(trueColor432, trueColor432Vis, 'True Color (432)')\n",
    "m\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "q_MEBIGnyp92",
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "<h6 style='color:#a28089; font-size:1.5rem; font-weight:bold; line-height:2rem;'>4. 맵(Map) 시각화</h6>\n",
    "<div style='margin:auto; width:90%; margin-top:3rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>해저지형도 제작</p>\n",
    "    <ul style='font-size:2rem;line-height:3rem'>\n",
    "        <li>GEE에서 제공하는 <a href='https://developers.google.com/earth-engine/datasets/catalog/NOAA_NGDC_ETOPO1#bands'>ETOPO1</a>의 수심자료를 이용하여 우리나라 주변해역에 대한 해저지형도를 그려보자.</li>\n",
    "        <li><a href='https://developers.google.com/earth-engine/datasets/catalog/NOAA_NGDC_ETOPO1#bands'>ETOPO1</a>: ETOPO1은 지구 표면의 1 각분(arc-minute) 해상도의 글로벌 지형 모델로, 육상 지형과 해양 수심을 통합한 데이터임. 이 모델은 다양한 글로벌 및 지역 데이터 세트를 바탕으로 구축되었으며 ETOPO1은 두 가지 고도 밴드 'ice_surface'와 'bedrock'을 포함하고 있음</li>\n",
    "        <li>참고로, 다운받은 EEZ 자료를 자신 계정의 GEE Asset에 업로드하면 해당 Asset ID로 접근하여 이용할 수 있다.</li>\n",
    "    </ul>           \n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "VIiyf6azf4mU",
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [],
   "source": [
    "# 우리나라 관할해역\n",
    "eez = ee.FeatureCollection(\"projects/ee-haebom/assets/kr_eez\")\n",
    "etopo = ee.Image('NOAA/NGDC/ETOPO1');\n",
    "elevation = etopo.select('bedrock');\n",
    "bathy = elevation.updateMask(elevation.lt(0));\n",
    "\n",
    "# Set visualization parameters.\n",
    "bathyVis = {\n",
    "  'min': -7000.0,\n",
    "  'max': 0.0,\n",
    "  'palette': cm.palettes.gist_earth } # gist_earth는 GEEMAP 라이브러리에서 제공하는 팔레트\n",
    "\n",
    "\n",
    "# Map 객체 생성\n",
    "Map = geemap.Map(center=[37, 129], zoom=7)\n",
    "\n",
    "# Map 객체에 bathymetry 레이어 추가\n",
    "Map.addLayer(bathy, bathyVis, 'bathymetry')\n",
    "\n",
    "# Map 객체에 EEZ 레이어 추가\n",
    "Map.addLayer(eez, {}, 'eez')\n",
    "\n",
    "# Map 표출\n",
    "display(Map)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "HqyCG_2Cyp92",
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "<h6 style='color:#a28089; font-size:1.5rem; font-weight:bold; line-height:2rem;'>4. 맵(Map) 시각화</h6>\n",
    "<div style='margin:auto; width:90%; margin-top:3rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>등수심선(depth contour line) 그리기</p>\n",
    "    <ul style='font-size:2rem;'>\n",
    "        <li>등수심선을 추가하여 해저지형을 상세하게 살펴보자.</li> \n",
    "    </ul>\n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 17
    },
    "id": "Qhv4AIsIvpfX",
    "outputId": "dbdac1cf-21c3-4298-f05f-ace87690568c",
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "            <style>\n",
       "                .geemap-dark {\n",
       "                    --jp-widgets-color: white;\n",
       "                    --jp-widgets-label-color: white;\n",
       "                    --jp-ui-font-color1: white;\n",
       "                    --jp-layout-color2: #454545;\n",
       "                    background-color: #383838;\n",
       "                }\n",
       "\n",
       "                .geemap-dark .jupyter-button {\n",
       "                    --jp-layout-color3: #383838;\n",
       "                }\n",
       "\n",
       "                .geemap-colab {\n",
       "                    background-color: var(--colab-primary-surface-color, white);\n",
       "                }\n",
       "\n",
       "                .geemap-colab .jupyter-button {\n",
       "                    --jp-layout-color3: var(--colab-primary-surface-color, white);\n",
       "                }\n",
       "            </style>\n",
       "            "
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "# 등심선(contour line) 생성 함수\n",
    "def contour_f(line):\n",
    "  binary_contour = bathy.convolve(ee.Kernel.gaussian(7, 5)).subtract(ee.Image.constant(line)).zeroCrossing()\n",
    "  return binary_contour.multiply(ee.Image.constant(line)).toFloat().mask(binary_contour)\n",
    "\n",
    "# 0에서 -4000미터 수심까지 50m 간격으로 등수심선 생성\n",
    "lines = ee.List.sequence(-4000, 0, 50)\n",
    "contourlines = lines.map(contour_f)\n",
    "contourlines = ee.ImageCollection(contourlines).mosaic()\n",
    "\n",
    "# 생성된 등수심선을 관할해역(EEZ)영역으로 클립핑(clip)\n",
    "contourlines = contourlines.clip(eez);\n",
    "\n",
    "# 등수심성을 레이어로 추가\n",
    "# gist_earth_r은 gist_earth 색상의 역순(reverse)를 의미함\n",
    "Map.addLayer(contourlines, {'min': -4000, 'max': 0, 'palette': cm.palettes.gist_earth_r}, 'contours') #['00ff00', 'ff0000']\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "AiNL066NQ-jt",
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "<h6 style='color:#a28089; font-size:1.5rem; font-weight:bold; line-height:4rem;'>4. 맵(Map) 시각화</h6>\n",
    "<div style='margin:auto; width:90%; margin-top:3rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>우리나라 바다의 최저 수심지역 찾기</p>\n",
    "    <ul style='font-size:2rem;line-height:3rem;'>\n",
    "        <li><code>Reducer</code>: 어스엔진에서 시간, 공간, 밴드, 배열과 같이 각각의 구조화된 데이터를 집계하는 함수</li> \n",
    "        <ul>\n",
    "            <li><code>reduceRegion()</code></li> \n",
    "            <li><code>ee.Reducer.min()</code></li>\n",
    "        </ul>\n",
    "         <li>좌표를 geemap의 maker를 이용하여 지도 상에 표시하기</li> \n",
    "         <li>인터넷 검색결과와 비교해 보기</li> \n",
    "    </ul>\n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "q-itcBxeF5Kf",
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [],
   "source": [
    "lonLatImage = ee.Image.pixelLonLat();\n",
    "bathyWithLonLat = bathy.addBands(lonLatImage);\n",
    "# EEZ 영역에 대한 수심을 집계하여 최저수심을 찾는다.\n",
    "bathy_stats = bathyWithLonLat.reduceRegion(\n",
    "    reducer=ee.Reducer.min(3),\n",
    "    geometry=eez,\n",
    "    scale=1000,        # bathy data의 resolution\n",
    "    crs= 'EPSG:4326',  # crs(좌표참조시스템)는 EPSG:4326, 즉 WGS84 좌표계를 적용했음을 의미\n",
    ")\n",
    "# 최저수심과 해당 좌표를 출력\n",
    "print(bathy_stats.getInfo())\n",
    "\n",
    "min_depth = bathy_stats.getInfo()['min']\n",
    "x_min = bathy_stats.getInfo()['min1']\n",
    "y_min = bathy_stats.getInfo()['min2']\n",
    "# 지도 상에 최조수심 위치를 마커로 표시하기\n",
    "Map.add_marker(\n",
    "    [y_min, x_min],\n",
    "    shape=\"circle\",\n",
    "    radius=20,\n",
    "    color=\"red\",\n",
    "    fill_color=\"#3388ff\",\n",
    "    fill_opacity=0.5,)\n",
    "Map"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "tZrxJebdVRpI",
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "<h3 style='color:#a28089; font-size:3rem; font-weight:bold; line-height:4rem;'>5. Wrap up</h3>\n",
    "<div style='margin:auto; width:90%; margin-top:3rem;'>\n",
    "    <p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;'>해저지형도 어디에 쓰나?</p>\n",
    "    <ul style='font-size:2rem;'>\n",
    "        <li style='line-height:4rem;'>참고자료:<a href='https://blog.naver.com/koreamof/221913422494'>국가해양기본도</a></li>\n",
    "    </ul>\n",
    "</div>\n",
    "<div style='margin:auto; text-align:center; width:50%;margin-bottom:5rem'>\n",
    "    <img src='https://github.com/Marino89/teacher_training/blob/main/image/bathy_chart.png?raw=true'>\n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "2CbgsMGUyp93",
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "<div style='margin-left:2rem;'>\n",
    "<p style='color:#a28089; font-size:3rem; font-weight:bold; line-height:4rem;'>참고자료</p>\n",
    "<p style='color:#a0d2eb; font-size:2.5rem; font-weight:bold; line-height:2rem;padding-left:5rem'>Markdwon</p>\n",
    "<ul style='padding-left:8rem;'>\n",
    "    <li><a href=''>https://colab.research.google.com/github/Tanu-N-Prabhu/Python/blob/master/Cheat_sheet_for_Google_Colab.ipynb</a></li>\n",
    "    <li><a href=''>https://colab.research.google.com/notebooks/markdown_guide.ipynb</a></li>\n",
    "</ul>\n",
    "</div>\n",
    "<footer>\n",
    "    <p style='font-size:1rem;text-align:right;'>&copy; 2024 Haebomdata Inc. All rights reserved.</p>\n",
    "</footer>"
   ]
  }
 ],
 "metadata": {
  "celltoolbar": "Slideshow",
  "colab": {
   "provenance": []
  },
  "hide_input": false,
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  },
  "nbTranslate": {
   "displayLangs": [
    "*"
   ],
   "hotkey": "alt-t",
   "langInMainMenu": true,
   "sourceLang": "en",
   "targetLang": "fr",
   "useGoogleTranslate": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
