/zfssz3/SP_MSI/Pipeline/software/application/wkhtmltox/bin/wkhtmltopdf-amd64 --disable-external-links  --print-media-type -O Portrait --encoding UTF-8 --footer-font-size 10 --footer-spacing 0 -T 30mm -R 22mm -B 41mm -L 22mm --cover ./submit/pdf/images/cover.html  --page-offset 1 --footer-center '[page]/[toPage]' --footer-spacing 10 --outline  --toc -R 10 --toc-header-text Contents --toc-l1-font-size 12 --toc-l1-indentation 50 --toc-l2-font-size 10 --toc-l2-indentation 60 --toc-l3-font-size 10 --toc-l3-indentation 70 ./submit/pdf/content.html ./submit/pdf/PDF1.pdf 
/zfssz3/SP_MSI/Pipeline/software/application/pdftk/pdftk  ./submit/pdf/PDF1.pdf background ./submit/pdf/images/background.pdf output ./submit/pdf/PDF2.pdf
/zfssz3/SP_MSI/Pipeline/software/application/pdftk/pdftk  ./submit/pdf/PDF2.pdf  ./submit/pdf/images/bottom.pdf output ./submit/correlation_analysis_report.pdf
rm ./submit/pdf/PDF1.pdf ./submit/pdf/PDF2.pdf

