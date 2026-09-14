---
title: La clase Imagick
source_url: https://www.php.net/manual/es/class.imagick.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 4d17b7b49
order: 36130
---

## Sinopsis de la clase

Imagick

Imagick

Iterator

## Métodos de imagen y métodos globales

La clase Imagick permite actuar sobre varias imágenes simultáneamente y esto, gracias a una pila interna. Siempre hay un puntero interno, apuntando a la imagen actual. Algunas funciones actúan sobre todas las imágenes de una clase Imagick, pero la mayoría únicamente sobre la imagen actual en relación con esta pila. Al igual que las conversiones, los nombres de los métodos pueden contener el nombre de la imagen, relatando únicamente el efecto sobre la imagen de la pila.

## Métodos de la clase

Dado el número de métodos, aquí se presenta una lista que los muestra de forma general:

| Efectos sobre la imagen | Métodos de recuperación | Métodos de definición | Lectura/escritura de la imagen | Otros |
|----|----|----|----|----|
| Imagick::adaptiveBlurImage | Imagick::getCompression | Imagick::setBackgroundColor | Imagick::\_\_construct | Imagick::clear |
| Imagick::adaptiveResizeImage | Imagick::getFilename | Imagick::setCompressionQuality | Imagick::addImage | Imagick::clone |
| Imagick::adaptiveSharpenImage | Imagick::getFormat | Imagick::setCompression | Imagick::appendImages | Imagick::current |
| Imagick::adaptiveThresholdImage | Imagick::getImageBackgroundColor | Imagick::setFilename | Imagick::getFilename | Imagick::destroy |
| Imagick::addNoiseImage | Imagick::getImageBlob | Imagick::getImagesBlob | Imagick::setFormat | Imagick::getFormat |
| Imagick::affinetransformimage | Imagick::getImageBluePrimary | Imagick::setImageBackgroundColor | Imagick::getImageFilename | Imagick::getHomeURL |
| Imagick::annotateImage | Imagick::getImageBorderColor | Imagick::setFirstIterator | Imagick::getImageFormat | Imagick::commentImage |
| Imagick::averageImages | Imagick::getImageChannelDepth | Imagick::setImageBias | Imagick::getImage | Imagick::getNumberImages |
| Imagick::blackThresholdImage | Imagick::getImageChannelDistortion | Imagick::setImageBluePrimary | Imagick::setImageFilename | Imagick::getReleaseDate |
| Imagick::blurImage | Imagick::getImageChannelExtrema | Imagick::setImageBorderColor | Imagick::setImageFormat | Imagick::getVersion |
| Imagick::borderImage | Imagick::getImageChannelMean | Imagick::setImageChannelDepth | Imagick::readImageFile | Imagick::hasNextImage |
| Imagick::charcoalImage | Imagick::getImageChannelStatistics | Imagick::setImageColormapColor | Imagick::readImage | Imagick::hasPreviousImage |
| Imagick::chopImage | Imagick::getImageColormapColor | Imagick::setImageColorSpace | Imagick::writeImages | Imagick::labelImage |
| Imagick::clipImage | Imagick::getImageColorspace | Imagick::setImageCompose | Imagick::writeImage | Imagick::newImage |
| Imagick::clipPathImage | Imagick::getImageColors | Imagick::setImageCompression |  | Imagick::newPseudoImage |
| Imagick::coalesceImages | Imagick::getImageCompose | Imagick::setImageDelay |  | Imagick::nextImage |
| Imagick::colorFloodFillImage | Imagick::getImageDelay | Imagick::setImageDepth |  | Imagick::pingImageBlob |
| Imagick::colorizeImage | Imagick::getImageDepth | Imagick::setImageDispose |  | Imagick::pingImageFile |
| Imagick::combineImages | Imagick::getImageDispose | Imagick::setImageDispose |  | Imagick::pingImage |
| Imagick::compareImageChannels | Imagick::getImageDistortion | Imagick::setImageExtent |  | Imagick::previousImage |
| Imagick::compareImageLayers | Imagick::getImageExtrema | Imagick::setImageFilename |  | Imagick::profileImage |
| Imagick::compositeImage | Imagick::getImageFilename | Imagick::setImageFormat |  | Imagick::queryFormats |
| Imagick::contrastImage | Imagick::getImageFormat | Imagick::setImageGamma |  | Imagick::removeImageProfile |
| Imagick::contrastStretchImage | Imagick::getImageGamma | Imagick::setImageGreenPrimary |  | Imagick::removeImage |
| Imagick::convolveImage | Imagick::getImageGeometry | Imagick::setImageIndex |  | Imagick::setFirstIterator |
| Imagick::cropImage | Imagick::getImageGreenPrimary | Imagick::setImageInterpolateMethod |  | Imagick::setImageIndex |
| Imagick::cycleColormapImage | Imagick::getImageHeight | Imagick::setImageIterations |  | Imagick::valid |
| Imagick::deconstructImages | Imagick::getImageHistogram | Imagick::setImageMatteColor |  | Imagick::getCopyright |
| Imagick::drawImage | Imagick::getImageIndex | Imagick::setImageMatte |  |  |
| Imagick::edgeImage | Imagick::getImageInterlaceScheme | Imagick::setImagePage |  |  |
| Imagick::embossImage | Imagick::getImageInterpolateMethod | Imagick::setImageProfile |  |  |
| Imagick::enhanceImage | Imagick::getImageIterations | Imagick::setImageProperty |  |  |
| Imagick::equalizeImage | Imagick::getImageMatteColor | Imagick::setImageRedPrimary |  |  |
| Imagick::evaluateImage | Imagick::getImageMatte | Imagick::setImageRenderingIntent |  |  |
| Imagick::flattenImages | Imagick::getImagePage | Imagick::setImageResolution |  |  |
| Imagick::flipImage | Imagick::getImagePixelColor | Imagick::setImageScene |  |  |
| Imagick::flopImage | Imagick::getImageProfile | Imagick::setImageTicksPerSecond |  |  |
|  | Imagick::getImageProperty | Imagick::setImageType |  |  |
| Imagick::fxImage | Imagick::getImageRedPrimary | Imagick::setImageUnits |  |  |
| Imagick::gammaImage | Imagick::getImageRegion | Imagick::setImageVirtualPixelMethod |  |  |
| Imagick::gaussianBlurImage | Imagick::getImageRenderingIntent | Imagick::setImageWhitepoint |  |  |
| Imagick::implodeImage | Imagick::getImageResolution | Imagick::setInterlaceScheme |  |  |
| Imagick::levelImage | Imagick::getImageScene | Imagick::setOption |  |  |
| Imagick::linearStretchImage | Imagick::getImageSignature | Imagick::setPage |  |  |
| Imagick::magnifyImage | Imagick::getImageTicksPerSecond | Imagick::setResolution |  |  |
| Imagick::matteFloodFillImage | Imagick::getImageTotalInkDensity | Imagick::setResourceLimit |  |  |
| Imagick::medianFilterImage | Imagick::getImageType | Imagick::setSamplingFactors |  |  |
| Imagick::minifyImage | Imagick::getImageUnits | Imagick::setSizeOffset |  |  |
| Imagick::modulateImage | Imagick::getImageVirtualPixelMethod | Imagick::setSize |  |  |
| Imagick::montageImage | Imagick::getImageWhitepoint | Imagick::setType |  |  |
| Imagick::morphImages | Imagick::getImageWidth |  |  |  |
| Imagick::mosaicImages | Imagick::getImage |  |  |  |
| Imagick::motionBlurImage | Imagick::getInterlaceScheme |  |  |  |
| Imagick::negateImage | Imagick::getNumberImages |  |  |  |
| Imagick::normalizeImage | Imagick::getOption |  |  |  |
| Imagick::oilPaintImage | Imagick::getPackageName |  |  |  |
| Imagick::optimizeImageLayers | Imagick::getPage |  |  |  |
| Imagick::paintOpaqueImage | Imagick::getPixelIterator |  |  |  |
| Imagick::paintTransparentImage | Imagick::getPixelRegionIterator |  |  |  |
| Imagick::posterizeImage | Imagick::getQuantumDepth |  |  |  |
| Imagick::radialBlurImage | Imagick::getQuantumRange |  |  |  |
| Imagick::raiseImage | Imagick::getResourceLimit |  |  |  |
| Imagick::randomThresholdImage | Imagick::getResource |  |  |  |
| Imagick::reduceNoiseImage | Imagick::getSamplingFactors |  |  |  |
| Imagick::render | Imagick::getSizeOffset |  |  |  |
| Imagick::resampleImage | Imagick::getSize |  |  |  |
| Imagick::resizeImage | Imagick::identifyImage |  |  |  |
| Imagick::rollImage | Imagick::getImageSize |  |  |  |
| Imagick::rotateImage |  |  |  |  |
| Imagick::sampleImage |  |  |  |  |
| Imagick::scaleImage |  |  |  |  |
| Imagick::separateImageChannel |  |  |  |  |
| Imagick::sepiaToneImage |  |  |  |  |
| Imagick::shadeImage |  |  |  |  |
| Imagick::shadowImage |  |  |  |  |
| Imagick::sharpenImage |  |  |  |  |
| Imagick::shaveImage |  |  |  |  |
| Imagick::shearImage |  |  |  |  |
| Imagick::sigmoidalContrastImage |  |  |  |  |
| Imagick::sketchImage |  |  |  |  |
| Imagick::solarizeImage |  |  |  |  |
| Imagick::spliceImage |  |  |  |  |
| Imagick::spreadImage |  |  |  |  |
| Imagick::steganoImage |  |  |  |  |
| Imagick::stereoImage |  |  |  |  |
| Imagick::stripImage |  |  |  |  |
| Imagick::swirlImage |  |  |  |  |
| Imagick::textureImage |  |  |  |  |
| Imagick::thresholdImage |  |  |  |  |
| Imagick::thumbnailImage |  |  |  |  |
| Imagick::tintImage |  |  |  |  |
| Imagick::transverseImage |  |  |  |  |
| Imagick::trimImage |  |  |  |  |
| Imagick::uniqueImageColors |  |  |  |  |
| Imagick::unsharpMaskImage |  |  |  |  |
| Imagick::vignetteImage |  |  |  |  |
| Imagick::waveImage |  |  |  |  |
| Imagick::whiteThresholdImage |  |  |  |  |

Métodos de la clase {role="class"}
