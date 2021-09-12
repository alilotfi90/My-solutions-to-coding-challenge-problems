
    clc
 
    m=80;
    ncy=16;
    [U,X]=qr(randn(m));
    [V,X]=qr(randn(m));
    D(m,m)=0.;
    KX(ncy)=0.;
    ER(ncy)=0.;
    ER_HH(ncy)=0.0
    

for kcy=1:ncy
 
    KA=10^kcy;
    AL=log10(KA)/(m-1);
    KX(kcy)=log10(KA);
    ER(kcy)=KX(kcy)

    for i=1:m
        d(i)=10^(AL*(i-1));
        D(i,i)=d(i);
    end

    A=U*D*V';
    [Q,R]=qr(A);
    ER_HH(kcy)=norm(eye(m)-Q'*Q);
end

    KX
    ER_HH
    
    plot(KX,ER,'r--')
    hold on
    plot(KX,ER_HH,'b*')
    xlabel('log10(kA)')
    ylabel('I-QtQ')
    legend(' ','Householder')

