# TFTG_biobert


Code written during the GREEKC Malaga Hackathon
The objective was to generate features to train a BERT model for TFTG relation extraction
using this repository: https://github.com/dmis-lab/biobert v1.0
it makes very naive assumptions, considering only close entities and a window of words around them

to train the model (inside bert directory):
```bash
python3 tftg_bert.py
python3 run_re.py   --task_name=gad     --do_train=true     --do_eval=true     --do_predict=true \
                    --vocab_file=/biobert/pubmed_pmc_470k/vocab.txt     --bert_config_file=/biobert/pubmed_pmc_470k/bert_config.json \
                    --init_checkpoint=/biobert/pubmed_pmc_470k/biobert_model.ckpt     --max_seq_length=128     --train_batch_size=10 \
                    --learning_rate=2e-5     --num_train_epochs=3.0     --do_lower_case=false     --data_dir=TFTG_gad/ \
                    --output_dir=/tmp/RE_output/
```
