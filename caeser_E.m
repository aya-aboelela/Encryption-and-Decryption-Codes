function c=caeser_E(P,k)
c=double(P)+k;
i=find(c>122);
c(i)=c(i)-26;
i=find(c>90 & c<97);
c(i)=c(i)-26;
i=find(P==32);
c(i)=32;
c=char(c);
disp('plain text=')
disp(P)
disp('cipher text=')
disp(c)